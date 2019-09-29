  // page top
  // ====================
  $(window).scroll(function() {
      var scrollTop = $(window).scrollTop();

      if (scrollTop < 20) {
          if (!$("#pagetop").hasClass("hide")) {
              $("#pagetop").addClass("hide");
          }
      } else {
          if ($("#pagetop").hasClass("hide")) {
              $("#pagetop").removeClass("hide");
          }
      }
  });

  // Global Navigation Bar
  // ====================
  function gnbFnc() {
      var topnav = $('.topnav');
      var topnavs = topnav.find('li.topbtn');
      var topnavsA = topnavs.find('a');
      var topnavsUl = topnavs.find('ul');

      topnavs.bind('mouseenter', function() {
          topnavsA.removeClass('hover')
          topnavs.removeClass('on');
          $(this).addClass('on');
          topnavsUl.stop().animate({
              "height": 270 + "px",
              "padding-top": 0 + "px"
          }, 300);
      })

      topnav.bind('mouseleave focusout', function(e) {
          topnavsUl.stop().animate({
              "height": 0 + "px",
              "padding-top": 0 + "px"
          }, 300)
          topnavs.removeClass('on');
      })

      topnavsA.bind('focusin', function() {
          topnavs.removeClass('on');
          topnavsA.removeClass('hover')
          $(this).addClass('hover').closest('.topbtn').addClass('on')
          topnavsUl.stop().css({
              "height": 270 + "px",
              "padding-top": 0 + "px"
          }, 300);
      })
  }

  function gnb(dep1, dep2, dep3) {

      var $header = $("#header_wrap");
      var $gnb = $(".topnav");
      var $gnb_1dep = $(".topnav > li");
      var $gnb_2dep = $(".topnav > li > ul > li");

      $header.css({
          'height': '96px'
      });

      if (dep1) {

          $gnb_1dep.eq(dep1 - 1).addClass('active').attr('title', '현재 활성화 되어있는 1차 메뉴입니다.');


          if (dep2) {
              $gnb_1dep.eq(dep1 - 1).find('ul li').eq(dep2 - 1).find('a').addClass('active2').attr('title', '현재 활성화되어 있는 2차 메뉴입니다.');
          }
      }
      /* //gnb 리셋 */

      function lnb(dep1, dep2) {

          $('body').append("<div id='temp_lnb'></div>");
          var temp_lnb = $('#temp_lnb');

          var $lnb = $('.lnb'),
              $lnbBox = $('.leftmenu'),
              $lnb_1dep = $('.lnb > li'),
              $lnb_2dep = $('.lnb li .lnb_dep2 > li'),
              $onLnb_1dep = $lnb_1dep.eq(dep1 - 1),
              $onLnb_2dep = $lnb_1dep.eq(dep1 - 1).find('.lnb_dep2'),
              $lnb_1depBtn = $lnb_1dep.find('>a'),
              dep1Cnt = dep1,
              dep2Cnt = dep2

          //$lnb_1dep.find('img').clone().appendTo(temp_lnb)
          $lnb_1dep.find('img').each(function() {
              $(this).clone().appendTo(temp_lnb);
              $(this).clone().attr('src', on).appendTo(temp_lnb);
          })
          temp_lnb.remove();

          $('.lnb_dep2').hide();

          function initLnb() {
              //$('.lnb_dep2').css('display','none');
              //$('.lnb_dep2').stop().slideUp();
              $('.lnb_dep2').hide();

              $lnb_1dep.removeClass('on').find('> a > img').each(off)
              $lnb_1dep.eq(dep1 - 1).addClass('on').find('> a > img').each(on);

              if (dep2) {
                  //$onLnb_2dep.css('display','block');
                  //$onLnb_2dep.slideDown();
                  $onLnb_2dep.show();
                  $onLnb_2dep.find('li').eq(dep2 - 1).addClass('on').find('> a > img').each(on);
              }
          }

          initLnb();

          $lnb_1dep.bind('click', function(e) {
              //if( $(this).index() != dep1 - 1){
              e.stopPropagation();
              //$lnb_1dep.find('> a > img').each(off);
              $(this).siblings().find('> a > img').each(off);
              $(this).find('> a > img').each(on); // 2013-08-27
              $(this).addClass('active');
              //$(this).closest('li').siblings().find('ul').stop().slideUp();
              $(this).closest('li').siblings().find('ul').stop().hide();
              //$(this).find('ul').slideDown();
              $(this).find('ul').show();
              //}
          });

          $(window).bind('keyup', function(e) {
              if (e.keyCode == 16) {
                  isTab = false
              }
          })

          $lnb_1dep.find('>a').bind('keydown', function(e) {
              if ($(this).parent().index() != 0) {
                  if (e.keyCode == 9 && e.shiftKey) {
                      e.preventDefault();
                      $lnb_1dep.eq($(this).closest('li').index() - 1).find(' > a').trigger('focus').next('ul.lnb_dep2').find('li:last-child > a').focus();
                  }
              }
          })

          $lnb_1dep.bind('focusin', function(e) {
              //if( $(this).index() != dep1 - 1){
              e.stopPropagation();
              $lnb_1dep.find('> a > img').each(off);
              $(this).find('> a > img').each(on); // 2013-08-27
              $(this).addClass('active');
              $(this).closest('li').siblings().find('ul').stop().hide();
              $(this).find('ul').stop().show();
              //}
          });


          $lnb_2dep.bind('mouseenter focusin', function(e) {
              if (!$(this).hasClass('on')) {
                  $onLnb_2dep.find('li').removeClass('on');
                  $(this).find('> a > img').each(on); // 2013-08-27
                  $(this).addClass('on');
              }
          });

          $lnb_2dep.bind('mouseleave focusout', function(e) {
              //if( !$(this).hasClass('on')){
              $(this).removeClass('on');
              $(this).find('> a > img').each(off);
              //}
          });

          $lnbBox.bind('mouseleave', function(e) {
              initLnb();
          })


          $('ul.location li:first-child a').bind('focusin', function() {
              $('.lnb_dep2').hide();
              $lnb_1dep.find('> a > img').each(off);
              $lnb_1dep.eq(dep1 - 1).addClass('on').find('> a > img').each(on);

              if (dep2) {
                  $onLnb_2dep.show();
                  $onLnb_2dep.find('li').eq(dep2 - 1).addClass('on').find('> a > img').each(on);
              }
          })

          $lnb.find('li').eq(0).find('>a').bind('keydown', function(e) {
              if (e.keyCode == 9 && e.shiftKey) {
                  $('.lnb_dep2').hide();
                  $lnb_1dep.find('> a > img').each(off);
                  $lnb_1dep.eq(dep1 - 1).addClass('on').find('> a > img').each(on);
                  if (dep2) {
                      $onLnb_2dep.show();
                      $onLnb_2dep.find('li').eq(dep2 - 1).addClass('on').find('> a > img').each(on);
                  }
              }
          })
      }

      lnb(dep2, dep3);

  }

  /* on _ off javascript */
  function on() {
      this.src = this.src.replace("_off", "_on");
  }

  function off() {
      this.src = this.src.replace("_on", "_off");
  }


  /* skip navigation */
  function skip_navigating() {
      $("#skip_nav").attr("tabindex", 0).focus();
      $("a[href^='#']").click(function(evt) {
          var anchortarget = $(this).attr("href");
          if (anchortarget != "#") {
              $(anchortarget).attr("tabindex", 0).focus();
              $(anchortarget).removeAttr("tabindex");
          }

      });
      /*
      if (window.location.hash) {
      	$(window.location.hash).attr("tabindex", -1).focus();
      }
      */
      $("#skip_nav a").focus(function() {
          $("#skip_nav a").removeClass("on");
          $(this).addClass("on");
      })
      $("#skip_nav a").blur(function() {
          $("#skip_nav a").removeClass("on");
      })
  }

  /* 이미지 on off */
  function over_img(img, n) {

      if (n == "on") {
          var hover = "_on";
      } else {
          var hover = "_off";
      }
      if (img.parent().hasClass("home") == false && img.parent().hasClass("on") == false && img.hasClass("on") == false) {
          menuimg = img.find("img");
          if (menuimg.attr("src").indexOf(".jpg") > 0) {
              menuimg_type = ".jpg";
          } else if (menuimg.attr("src").indexOf(".gif") > 0) {
              menuimg_type = ".gif";
          } else if (menuimg.attr("src").indexOf(".png") > 0) {
              menuimg_type = ".png";
          }

          menuimg_src = menuimg.attr("src").split("_off")[0];
          menuimg_src = menuimg_src.split("_on")[0];
          menuimg.attr("src", menuimg_src + hover + menuimg_type);
      }
  }

  function selectBoxFnc() {
      var selSet = $('.select_set');
      var selOkBtn = selSet.find('a.select_ok');
      var selWrap = $('.select_wrap');

      selWrap.find('li.select_cell').eq(0).css({
          'display': 'block'
      });

      selOkBtn.bind('click', function() {
          var thisOption = selSet.find('select[name=input_select]').attr('value');
          selWrap.find('li.select_cell').hide();
          selWrap.find('li.cell_' + thisOption).show();
      })
  }

  $(function() {
      skip_navigating();
      //slideGallery(); // page call

      selectBoxFnc();
      gnbFnc();
      //tabbox();
  });






  /* Tab */
  +
  function($) {
      'use strict';

      // TAB CLASS DEFINITION
      // ====================

      var Tab = function(element) {
          this.element = $(element)
      }

      Tab.VERSION = '3.2.0'

      Tab.TRANSITION_DURATION = 150

      Tab.prototype.show = function() {
          var $this = this.element
          var $ul = $this.closest('ul:not(.dropdown-menu)')
          var selector = $this.data('target')

          if (!selector) {
              selector = $this.attr('href')
              selector = selector && selector.replace(/.*(?=#[^\s]*$)/, '') // strip for ie7
          }

          if ($this.parent('li').hasClass('active')) return

          var previous = $ul.find('.active:last a')[0]
          var e = $.Event('show.bs.tab', {
              relatedTarget: previous
          })

          $this.trigger(e)

          if (e.isDefaultPrevented()) return

          var $target = $(selector)

          this.activate($this.closest('li'), $ul)
          this.activate($target, $target.parent(), function() {
              $this.trigger({
                  type: 'shown.bs.tab',
                  relatedTarget: previous
              })
          })
      }

      Tab.prototype.activate = function(element, container, callback) {
          var $active = container.find('> .active')
          var transition = callback &&
              $.support.transition &&
              (($active.length && $active.hasClass('fade')) || !!container.find('> .fade').length)

          function next() {
              $active
                  .removeClass('active')
                  .find('> .dropdown-menu > .active')
                  .removeClass('active')

              element.addClass('active')

              if (transition) {
                  element[0].offsetWidth // reflow for transition
                  element.addClass('in')
              } else {
                  element.removeClass('fade')
              }

              if (element.parent('.dropdown-menu')) {
                  element.closest('li.dropdown').addClass('active')
              }

              callback && callback()
          }

          $active.length && transition ?
              $active
              .one('bsTransitionEnd', next)
              .emulateTransitionEnd(Tab.TRANSITION_DURATION) :
              next()

          $active.removeClass('in')
      }


      // TAB PLUGIN DEFINITION
      // =====================

      function Plugin(option) {
          return this.each(function() {
              var $this = $(this)
              var data = $this.data('bs.tab')

              if (!data) $this.data('bs.tab', (data = new Tab(this)))
              if (typeof option == 'string') data[option]()
          })
      }

      var old = $.fn.tab

      $.fn.tab = Plugin
      $.fn.tab.Constructor = Tab


      // TAB NO CONFLICT
      // ===============

      $.fn.tab.noConflict = function() {
          $.fn.tab = old
          return this
      }


      // TAB DATA-API
      // ============

      $(document).on('click.bs.tab.data-api', '[data-toggle="tab"], [data-toggle="pill"]', function(e) {
          e.preventDefault()
          Plugin.call($(this), 'show')
      })

  }(jQuery);



  //스크롤 이벤트 핸들링
  var timeout_sidebanner;
  $(window).scroll(function(e) {
      clearTimeout(timeout_sidebanner);
      timeout_sidebanner = setTimeout(function() {
          //사이드 퀵메뉴
          if ($('div.sub-qlink-wrap').length > 0) {
              if ($(window).scrollTop() > 178) {
                  $('div.sub-qlink-wrap').animate({
                      top: $(document).scrollTop() + 50
                  }, 500, function() {});
              } else {
                  $('div.sub-qlink-wrap').animate({
                      top: 178
                  }, 500, function() {});
              }
          }
      }, 100);
  });



  // CAROUSEL 
  +
  function($) {
      'use strict';

      // CAROUSEL CLASS DEFINITION
      // =========================

      var Carousel = function(element, options) {
          this.$element = $(element).on('keydown.bs.carousel', $.proxy(this.keydown, this))
          this.$indicators = this.$element.find('.carousel-indicators')
          this.options = options
          this.paused =
              this.sliding =
              this.interval =
              this.$active =
              this.$items = null

          this.options.pause == 'hover' && this.$element
              .on('mouseenter.bs.carousel', $.proxy(this.pause, this))
              .on('mouseleave.bs.carousel', $.proxy(this.cycle, this))
      }

      Carousel.VERSION = '3.2.0'

      Carousel.TRANSITION_DURATION = 600

      Carousel.DEFAULTS = {
          interval: 5000,
          pause: 'hover',
          wrap: true
      }

      Carousel.prototype.keydown = function(e) {
          switch (e.which) {
              case 37:
                  this.prev();
                  break
              case 39:
                  this.next();
                  break
              default:
                  return
          }

          e.preventDefault()
      }

      Carousel.prototype.cycle = function(e) {
          e || (this.paused = false)

          this.interval && clearInterval(this.interval)

          this.options.interval &&
              !this.paused &&
              (this.interval = setInterval($.proxy(this.next, this), this.options.interval))

          return this
      }

      Carousel.prototype.getItemIndex = function(item) {
          this.$items = item.parent().children('.item')
          return this.$items.index(item || this.$active)
      }

      Carousel.prototype.getItemForDirection = function(direction, active) {
          var delta = direction == 'prev' ? -1 : 1
          var activeIndex = this.getItemIndex(active)
          var itemIndex = (activeIndex + delta) % this.$items.length
          return this.$items.eq(itemIndex)
      }

      Carousel.prototype.to = function(pos) {
          var that = this
          var activeIndex = this.getItemIndex(this.$active = this.$element.find('.item.active'))

          if (pos > (this.$items.length - 1) || pos < 0) return

          if (this.sliding) return this.$element.one('slid.bs.carousel', function() {
              that.to(pos)
          }) // yes, "slid"
          if (activeIndex == pos) return this.pause().cycle()

          return this.slide(pos > activeIndex ? 'next' : 'prev', this.$items.eq(pos))
      }

      Carousel.prototype.pause = function(e) {
          e || (this.paused = true)

          if (this.$element.find('.next, .prev').length && $.support.transition) {
              this.$element.trigger($.support.transition.end)
              this.cycle(true)
          }

          this.interval = clearInterval(this.interval)

          return this
      }

      Carousel.prototype.next = function() {
          if (this.sliding) return
          return this.slide('next')
      }

      Carousel.prototype.prev = function() {
          if (this.sliding) return
          return this.slide('prev')
      }

      Carousel.prototype.slide = function(type, next) {
          var $active = this.$element.find('.item.active')
          var $next = next || this.getItemForDirection(type, $active)
          var isCycling = this.interval
          var direction = type == 'next' ? 'left' : 'right'
          var fallback = type == 'next' ? 'first' : 'last'
          var that = this

          if (!$next.length) {
              if (!this.options.wrap) return
              $next = this.$element.find('.item')[fallback]()
          }

          if ($next.hasClass('active')) return (this.sliding = false)

          var relatedTarget = $next[0]
          var slideEvent = $.Event('slide.bs.carousel', {
              relatedTarget: relatedTarget,
              direction: direction
          })
          this.$element.trigger(slideEvent)
          if (slideEvent.isDefaultPrevented()) return

          this.sliding = true

          isCycling && this.pause()

          if (this.$indicators.length) {
              this.$indicators.find('.active').removeClass('active')
              var $nextIndicator = $(this.$indicators.children()[this.getItemIndex($next)])
              $nextIndicator && $nextIndicator.addClass('active')
          }

          var slidEvent = $.Event('slid.bs.carousel', {
              relatedTarget: relatedTarget,
              direction: direction
          }) // yes, "slid"
          if ($.support.transition && this.$element.hasClass('slide')) {
              $next.addClass(type)
              $next[0].offsetWidth // force reflow
              $active.addClass(direction)
              $next.addClass(direction)
              $active
                  .one('bsTransitionEnd', function() {
                      $next.removeClass([type, direction].join(' ')).addClass('active')
                      $active.removeClass(['active', direction].join(' '))
                      that.sliding = false
                      setTimeout(function() {
                          that.$element.trigger(slidEvent)
                      }, 0)
                  })
                  .emulateTransitionEnd(Carousel.TRANSITION_DURATION)
          } else {
              $active.removeClass('active')
              $next.addClass('active')
              this.sliding = false
              this.$element.trigger(slidEvent)
          }

          isCycling && this.cycle()

          return this
      }


      // CAROUSEL PLUGIN DEFINITION
      // ==========================

      function Plugin(option) {
          return this.each(function() {
              var $this = $(this)
              var data = $this.data('bs.carousel')
              var options = $.extend({}, Carousel.DEFAULTS, $this.data(), typeof option == 'object' && option)
              var action = typeof option == 'string' ? option : options.slide

              if (!data) $this.data('bs.carousel', (data = new Carousel(this, options)))
              if (typeof option == 'number') data.to(option)
              else if (action) data[action]()
              else if (options.interval) data.pause().cycle()
          })
      }

      var old = $.fn.carousel

      $.fn.carousel = Plugin
      $.fn.carousel.Constructor = Carousel


      // CAROUSEL NO CONFLICT
      // ====================

      $.fn.carousel.noConflict = function() {
          $.fn.carousel = old
          return this
      }


      // CAROUSEL DATA-API
      // =================

      $(document).on('click.bs.carousel.data-api', '[data-slide], [data-slide-to]', function(e) {
          var href
          var $this = $(this)
          var $target = $($this.attr('data-target') || (href = $this.attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '')) // strip for ie7
          if (!$target.hasClass('carousel')) return
          var options = $.extend({}, $target.data(), $this.data())
          var slideIndex = $this.attr('data-slide-to')
          if (slideIndex) options.interval = false

          Plugin.call($target, options)

          if (slideIndex) {
              $target.data('bs.carousel').to(slideIndex)
          }

          e.preventDefault()
      })

      $(window).on('load', function() {
          $('[data-ride="carousel"]').each(function() {
              var $carousel = $(this)
              Plugin.call($carousel, $carousel.data())
          })
      })

  }(jQuery);


  /* Floating Report Menu */
  $(document).ready(function() {
      var fmenu = $('.fmenu').offset();
      $(window).scroll(function() {
          if ($(document).scrollTop() > 280) {
              $('.fmenu').addClass('fixed');
              $('.fmenu-space').addClass('fmenu-space-fixed');
          } else {
              $('.fmenu').removeClass('fixed');
              $('.fmenu-space').removeClass('fmenu-space-fixed');
          }
          if ($(document).scrollTop() > 180) {
              $('body').addClass('pdtop');
          } else {
              $('body').removeClass('pdtop');
          }
      });
      var famenu = $('.famenu').offset();
      $(window).scroll(function() {
          if ($(document).scrollTop() > 280) {
              $('.famenu').addClass('fafixed');
              $('.fmenu-space').addClass('fmenu-space-fixed');
              $('.famenu-title').addClass('famenu-title-fixed');
          } else {
              $('.famenu').removeClass('fafixed');
              $('.fmenu-space').removeClass('fmenu-space-fixed');
              $('.famenu-title').removeClass('famenu-title-fixed');
          }
          if ($(document).scrollTop() > 180) {
              $('body').addClass('fapdtop');
          } else {
              $('body').removeClass('fapdtop');
          }
      });
  });

  //각 보고서에서 탭 이동시 사용하는 함수
  function moveBtn(id) {
      var offset = $('#' + id).offset();
      $('html, body').animate({
          scrollTop: offset.top
      }, 400);
  }

  function loadingShow(time, reportNm) {
      $('#analyNm').html(reportNm);

      $('#loadingPer').show();

      $("#pBar").data("origWidth", $('#pBar').width()).width(0).animate({
          width: $('#pBar').data("origWidth")
      }, time);

      $('#numPer').prop('number', 10).animateNumber({
          number: 97
      }, time);
  }

  function loadingHide() {
      $('#loadingPer').hide();
  }