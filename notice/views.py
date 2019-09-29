import re

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView

from notice.forms import NoticeForm
from notice.models import Notice


from django.shortcuts import render, redirect


# 공지사항

def notice_list(request):
    qs = Notice.objects.filter(board__contains='공지사항')
    return render(request, 'notice/notice_list.html',
                  {'notice_list': qs})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    is_liked = False
    if notice.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'notice': notice,
        'is_liked': is_liked,
        'total_likes': notice.total_likes(),
    }
    return render(request, 'notice/notice_detail.html',
                  context)

def notice_new(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('notice:notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'notice/notice_form.html', {'form':form})

def notice_edit(request, pk):
    item = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST or None, instance=item)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()  # 저장하기
        return redirect('/notice/' + str(item.id))
    return render(request, 'notice/notice_form.html', {'form':form})


def notice_remove(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('notice:notice_list')
#


# 여기부터 프랜차이즈
def franchise_list(request):
    qs = Notice.objects.filter(board__contains='프랜차이즈')
    return render(request, 'notice/franchise_list.html',
                  {'franchise_list': qs})

def franchise_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notice/franchise_detail.html',
                  {'notice': notice})

# 프랜차이즈 게시글 수정 삭제 등록
def franchise_new(request, notice=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        title = data.get('title')
        content = data.get('content')
        photo = files.get('photo')
        board = data.get('board')

        # 유효성 검사
        if len(title) == 0:
            error_list.append('title을 1글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', content):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if notice is None:
                notice = Notice()

            notice.title = title
            notice.content = content
            if photo:
                notice.photo.save(photo.name, photo, save=False)

            try:
                notice.save()
            except Exception as e:
                error_list.append(e)
            else:
                # return redirect(item)  # item.get_absolute_url 호출됨
                return redirect('notice:franchise_list')

        initial = {
            'title': title,
            'content': content,
            'photo': photo,
            'board': board,
        }
    else:
        if notice is not None:
            initial = {
                'title': notice.title,
                'content': notice.content,
                'photo': notice.photo,
                'board': notice.board,
            }
    return render(request, 'notice/franchise_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def franchise_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return franchise_new(request, notice)


def franchise_remove(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('notice:franchise_list')
#
# # 프랜차이즈 게시글 수정 삭제 등록
# def franchise_new(request, notice=None):
#     error_list = []
#     initial = {}
#
#     if request.method == 'POST':
#         data = request.POST
#         files = request.FILES
#
#         title = data.get('title')
#         content = data.get('content')
#         photo = files.get('photo')
#         board = data.get('board')
#
#         # 유효성 검사
#         if len(title) == 0:
#             error_list.append('title을 1글자 이상 입력해주세요.')
#
#         if re.match(r'^[\da-zA-Z\s]+$', content):
#             error_list.append('한글을 입력해주세요.')
#
#         if not error_list:
#             # 저장 시도
#             if notice is None:
#                 notice = Notice()
#
#             notice.title = title
#             notice.content = content
#             if photo:
#                 notice.photo.save(photo.name, photo, save=False)
#
#             try:
#                 notice.save()
#             except Exception as e:
#                 error_list.append(e)
#             else:
#                 # return redirect(item)  # item.get_absolute_url 호출됨
#                 return redirect('notice:franchise_list')
#
#         initial = {
#             'title': title,
#             'content': content,
#             'photo': photo,
#             'board': board,
#         }
#     else:
#         if notice is not None:
#             initial = {
#                 'title': notice.title,
#                 'content': notice.content,
#                 'photo': notice.photo,
#                 'board': notice.board,
#             }
#     return render(request, 'notice/franchise_form.html', {
#         'error_list': error_list,
#         'initial': initial,
#     })
#
#
# def franchise_edit(request, pk):
#     notice = get_object_or_404(Notice, pk=pk)
#     return franchise_new(request, notice)
#
#
# def franchise_remove(request, pk):
#     notice = get_object_or_404(Notice, pk=pk)
#     notice.delete()
#     return redirect('notice:franchise_list')
#

def like_notice(request):
    notice = get_object_or_404(Notice, id=request.POST.get('notice_id'))
    is_liked = False
    if notice.likes.filter(id=request.user.id).exists():
        notice.likes.remove(request.user)
        is_liked = False
    else:
        notice.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(notice.get_absolute_url())

#
#
#
#







