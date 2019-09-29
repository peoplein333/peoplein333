import re
from django.shortcuts import render, get_object_or_404, redirect

from notice.models import Notice
from .models import Item

from .forms import ItemForm

# from .forms import ItemForm

def item_new(request, item=None):
    if request.method == 'POST':                        # 'POST' 요청이면
        form = ItemForm(request.POST, request.FILES)    # 값을 가진 폼 생성
        if form.is_valid():         # 유효성 검사 통과하면
            item = form.save()      # ModelForm 기능을 이용해서 DB 저장
            return redirect(item)   # 저장된 item 보여주기
    else:                                               # 'POST' 요청 아니면
        form = ItemForm()                               # 빈 폼 생성

    return render(request, 'forSale/item_form.html', {
        'form': form,               # form 자체만 맥락 변수로 전달
    })




def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)


def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('forSale:item_list')



def item_list(request):
    items = Item.objects.all()
    # 키값이 'q'로 지정된 값이 없으면 None이 반환됨
    q = request.GET.get('q', '')  # 'q'로 지정된 값이 없으면 '' 반환
    if q:  # q가 널 아니면 qs에 filter 조건 추가
        items = items.filter(name__icontains=q)
    return render(request, 'forSale/item_list.html', {
        'item_list': items,
        'q': q, })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'forSale/item_detail.html',
                  {'item': item})


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
