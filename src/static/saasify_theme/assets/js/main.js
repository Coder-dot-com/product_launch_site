/***************************************************
==================== JS INDEX ======================
****************************************************
01. PreLoader Js


****************************************************/

(function ($) {
    ("use strict");

    var windowOn = $(window);
    // 01. PreLoader Js
    windowOn.on("load", function () {
        $("#loading").fadeOut(500);
    });
    if ($("#loading").length > 0) {
        $(".closeLoader").each(function () {
            $(this).on("click", function (e) {
                e.preventDefault();
                $("#loading").fadeOut(500);
            });
        });
    }

    // Mobile Menu
    $("#main-menu").meanmenu({
        meanMenuContainer: "#mobile-navbar-menu",
        meanScreenWidth: "991",
        meanExpand: ["<i class='fa-light fa-plus'></i> <i class='fa-light fa-minus'></i>"],
    });

    //canvas sidebar
    var canva_expander = $(".canva_expander");
    if (canva_expander.length) {
        $(".canva_expander, #canva_close, #tj-overlay-bg2").on("click", function (e) {
            e.preventDefault();
            $("body").toggleClass("canvas_expanded");
        });
    }

    //  search bar
    $(".search-btn").on("click", function () {
        $(".search_popup").addClass("search-opened");
        $(".search-popup-overlay").addClass("search-popup-overlay-open");
    });

    $(".search_close_btn").on("click", function () {
        $(".search_popup").removeClass("search-opened");
        $(".search-popup-overlay").removeClass("search-popup-overlay-open");
    });

    $(".search-popup-overlay").on("click", function () {
        $(".search_popup").removeClass("search-opened");
        $(this).removeClass("search-popup-overlay-open");
    });

    // Header Sticky  Js
    windowOn.on("scroll", function () {
        var scroll = $(window).scrollTop();
        if (scroll < 100) {
            $("#tj-header-sticky").removeClass("tj-header-sticky");
        } else {
            $("#tj-header-sticky").addClass("tj-header-sticky");
        }
    });

    // background image
    $("[data-bg-image]").each(function () {
        var $this = $(this),
            $image = $this.data("bg-image");
        $this.css("background-image", "url(" + $image + ")");
    });

    // Banner Slider
    var banner = new Swiper(".tj-banner-slider", {
        slidesPerView: 1,
        spaceBetween: 30,
        autoplay: {
            delay: 8500,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        loop: true,
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            640: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 1,
            },
            992: {
                slidesPerView: 1,
            },
            1024: {
                slidesPerView: 1,
            },
        },
    });

    // Team Slider
    var team = new Swiper(".tj-team-slider", {
        slidesPerView: 2,
        spaceBetween: 30,
        autoplay: {
            delay: 8500,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        loop: true,
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            640: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 2,
            },
        },
    });

    // Testimonial Slider
    var testimonial = new Swiper(".tj-testimonial-slider", {
        slidesPerView: 2,
        spaceBetween: 30,
        loop: true,
        autoplay: {
            delay: 8500,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            640: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 1,
            },
            992: {
                slidesPerView: 1,
            },
            1024: {
                slidesPerView: 1,
            },
        },
    });

    // Roll slider
    var roll_slider = new Swiper(".roll-slider", {
        spaceBetween: 0,
        centeredSlides: true,
        speed: 6000,
        autoplay: {
            delay: 1,
        },
        loop: true,
        slidesPerView: "auto",
        allowTouchMove: false,
        disableOnInteraction: true,
    });

    var roll_slider2 = new Swiper(".roll-slider2", {
        spaceBetween: 0,
        centeredSlides: true,
        speed: 6000,
        autoplay: {
            delay: 1,
            reverseDirection: true,
        },
        loop: true,
        loopedSlides: 4,
        slidesPerView: "auto",
        allowTouchMove: false,
        disableOnInteraction: true,
    });

    // Fun Fact
    $(".odometer").appear(function () {
        var odo = $(".odometer");
        odo.each(function () {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });

    // video js
    var popupvideos = $(".popup-videos-button");
    if (popupvideos.length) {
        $(".popup-videos-button").magnificPopup({
            disableOn: 10,
            type: "iframe",
            mainClass: "mfp-fade",
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false,
        });
    }

    // Sal Animation
    sal({
        threshold: 0.1,
        once: true,
    });

    // scrollTop init
    var saasifyScrollTop = document.querySelector(".saasify-scroll-top");
    if (saasifyScrollTop != null) {
        var scrollProgressPatch = document.querySelector(".saasify-scroll-top path");
        var pathLength = scrollProgressPatch.getTotalLength();
        var offset = 50;
        scrollProgressPatch.style.transition = scrollProgressPatch.style.WebkitTransition = "none";
        scrollProgressPatch.style.strokeDasharray = pathLength + " " + pathLength;
        scrollProgressPatch.style.strokeDashoffset = pathLength;
        scrollProgressPatch.getBoundingClientRect();
        scrollProgressPatch.style.transition = scrollProgressPatch.style.WebkitTransition =
            "stroke-dashoffset 10ms linear";
        window.addEventListener("scroll", function (event) {
            var scroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var progress = pathLength - (scroll * pathLength) / height;
            scrollProgressPatch.style.strokeDashoffset = progress;
            var scrollElementPos = document.body.scrollTop || document.documentElement.scrollTop;
            if (scrollElementPos >= offset) {
                saasifyScrollTop.classList.add("progress-done");
            } else {
                saasifyScrollTop.classList.remove("progress-done");
            }
        });
        saasifyScrollTop.addEventListener("click", function (e) {
            e.preventDefault();
            window.scroll({
                top: 0,
                left: 0,
                behavior: "smooth",
            });
        });
    }
    /*-- saasify scroll top scripts end --*/
})(jQuery);
