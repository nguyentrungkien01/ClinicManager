(function ($) {
    "use strict";
    var healthcare = {
        initialised: false,
        version: 1.0,
        Solar: false,
        init: function () {

            if (!this.initialised) {
                this.initialised = true;
            } else {
                return;
            }

            // Functions Calling
            this.menu_toggle();
            this.submenu();
            this.counter();
            this.testimonial_thumb();
            this.go_top();
            this.preloader();
        },

        // menu toggle start
        menu_toggle: function () {
            if ($(".hc-main-header").length > 0) {
                $(".hc-menu-toggle").on('click', function (e) {
                    event.stopPropagation();
                    $(".hc-main-header").toggleClass("hc-open-menu");
                });
                $("body").on('click', function () {
                    $(".hc-main-header").removeClass("hc-open-menu");
                });
                $(".hc-navbar").on('click', function () {
                    event.stopPropagation();
                });
            };
        },
        // menu toggle end
        
        // menu submenu start
        submenu: function () {
            if ($(".hc-has-submenu").length > 0) {
                $(".hc-has-submenu").on('click', function () {
                    $(".hc-submenu").slideToggle();
                });
            };
        },
        // menu submenu end

        // counter start
        counter: function () {
            if ($('.hc-counter').length > 0) {
                var a = 0;
                $(window).scroll(function () {
                    var oTop = $('#counter').offset().top - window.innerHeight;
                    if (a == 0 && $(window).scrollTop() > oTop) {
                        $('.counter-value').each(function () {
                            var $this = $(this),
                                countTo = $this.attr('data-count');
                            $({
                                countNum: $this.text()
                            }).animate({
                                countNum: countTo
                            }, {
                                duration: 5000,
                                easing: 'swing',
                                step: function () {
                                    $this.text(Math.floor(this.countNum));
                                },
                                complete: function () {
                                    $this.text(this.countNum);
                                }
                            });
                        });
                        a = 1;
                    }
                });
            }
        },
        // counter end
        // testimonial start
        testimonial_thumb: function () {
            if ($('.hc-testi-slide').length > 0) {
                var galleryTop = new Swiper('.hc-testi-slide .gallery-top', {
                    spaceBetween: 10,
                    loop: true,
                    speed: 800,
                    autoplay: {
                        delay: 2500,
                        disableOnInteraction: false,
                    },
                    touchRatio: 0,
                    loopedSlides: 5, //looped slides should be the same
                    navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                    },
                    thumbs: {
                        swiper: galleryThumbs,
                    },
                });
            }
            if ($('.hc-testi-thumb').length > 0) {
                var galleryThumbs = new Swiper('.hc-testi-thumb .gallery-thumbs', {
                    spaceBetween: 10,
                    slidesPerView: 3,
                    loop: true,
                    autoplay: {
                        delay: 2500,
                        disableOnInteraction: false,
                    },
                    speed: 800,
                    freeMode: true,
                    centeredSlides: true,
                    touchRatio: 0,
                    loopedSlides: 5,
                    navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                    },
                    effect: 'coverflow',
                    coverflowEffect: {
                        rotate: 0,
                        stretch: 420,
                        depth: 400,
                        modifier: 1,
                        slideShadows: true,
                    },
                    breakpoints: {
                        480: {
                            coverflowEffect: {
                                stretch: 500,
                            },
                        },
                        575: {
                            coverflowEffect: {
                                stretch: 500,
                            },
                        },
                        767: {
                            coverflowEffect: {
                                stretch: 260,
                            },
                        },
                        991: {
                            coverflowEffect: {
                                stretch: 330,
                            },
                        },
                    },
                });
            }
        },
        // testimonial end
        // go to start
        go_top: function () {
            $(window).on('scroll', function () {
                var scroll = $(window).scrollTop();
                if ($('.hc-main-header').length > 0) {
                    var header_height = $('.hc-main-header').innerHeight();
                    if (scroll >= header_height) {
                        $(".hc-main-header").addClass("hc-header-sticky");
                    } else {
                        $(".hc-main-header").removeClass("hc-header-sticky");
                    }
                }
                if ($('.hc-go-top').length > 0) {
                    if (scroll >= 300) {
                        $(".hc-go-top").addClass("hc-go-top-show");
                    } else {
                        $(".hc-go-top").removeClass("hc-go-top-show");
                    }
                }
                if ($('.hc-go-top').length > 0) {
                    $('.hc-go-top').on('click', function () {
                        $(window).scrollTop(0);
                    });
                }
            });
        },
        // go to end
        preloader: function () {
            jQuery("#status").fadeOut();
            jQuery("#hc-preloader").delay(350).fadeOut("slow");
        },
    };
    healthcare.init();
})(jQuery);

// init cursor
var cursors = [{
    cursor_id: "3",
    cursor_type: "0",
    cursor_shape: "15",
    cursor_image: "",
    default_cursor: "auto",
    hover_effect: "plugin",
    body_activation: "1",
    element_activation: "0",
    selector_type: "tag",
    selector_data: "body",
    color: "#cc3a3b",
    width: "30",
    blending_mode: "normal"
}];

window.onload = function () {
    $("#add_customer_result").modal("toggle");
};