"use strict";

$(".nav-search .input-group > input").focus(function (e) {
	$(this).parent().addClass("focus");
}).blur(function (e) {
	$(this).parent().removeClass("focus");
});

$('.table-responsive thead tr th').map(function () {
	if (($(this).text().trim() == "" && !$(this).find("input").length == 1))
		$(this).text('Thao tác')
})

$('.modal-dialog').removeClass('modal-xl')
$('.modal-dialog').addClass('modal-lg')

$(function () {
	$('[data-toggle="tooltip"]').tooltip();
	$('[data-toggle="popover"]').popover();
	layoutsColors();
});

function layoutsColors() {
	if ($('.sidebar').is('[data-background-color]')) {
		$('html').addClass('sidebar-color');
	} else {
		$('html').removeClass('sidebar-color');
	}

	if ($('body').is('[data-image]')) {
		$('body').css('background-image', 'url("' + $('body').attr('data-image') + '")');
	} else {
		$('body').css('background-image', '');
	}
}

function legendClickCallback(event) {
	event = event || window.event;

	var target = event.target || event.srcElement;
	while (target.nodeName !== 'LI') {
		target = target.parentElement;
	}
	var parent = target.parentElement;
	var chartId = parseInt(parent.classList[0].split("-")[0], 10);
	var chart = Chart.instances[chartId];
	var index = Array.prototype.slice.call(parent.children).indexOf(target);

	chart.legend.options.onClick.call(chart, event, chart.legend.legendItems[index]);
	if (chart.isDatasetVisible(index)) {
		target.classList.remove('hidden');
	} else {
		target.classList.add('hidden');
	}
}

$(document).ready(function () {

	$('.btn-refresh-card').on('click', function () {
		var e = $(this).parents(".card");
		e.length && (e.addClass("is-loading"), setTimeout(function () {
			e.removeClass("is-loading")
		}, 3e3))
	})

	var scrollbarDashboard = $('.sidebar .scrollbar');
	if (scrollbarDashboard.length > 0) {
		scrollbarDashboard.scrollbar();
	}

	var contentScrollbar = $('.main-panel .content-scroll');
	if (contentScrollbar.length > 0) {
		contentScrollbar.scrollbar();
	}

	var messagesScrollbar = $('.messages-scroll');
	if (messagesScrollbar.length > 0) {
		messagesScrollbar.scrollbar();
	}

	var tasksScrollbar = $('.tasks-scroll');
	if (tasksScrollbar.length > 0) {
		tasksScrollbar.scrollbar();
	}

	var quickScrollbar = $('.quick-scroll');
	if (quickScrollbar.length > 0) {
		quickScrollbar.scrollbar();
	}

	var messageNotifScrollbar = $('.message-notif-scroll');
	if (messageNotifScrollbar.length > 0) {
		messageNotifScrollbar.scrollbar();
	}

	var notifScrollbar = $('.notif-scroll');
	if (notifScrollbar.length > 0) {
		notifScrollbar.scrollbar();
	}

	var quickActionsScrollbar = $('.quick-actions-scroll');
	if (quickActionsScrollbar.length > 0) {
		quickActionsScrollbar.scrollbar();
	}

	var statsScrollbar = $('.stats-scroll');
	if (statsScrollbar.length > 0) {
		statsScrollbar.scrollbar();
	}

	$('.scroll-bar').draggable();

	$('#search-nav').on('shown.bs.collapse', function () {
		$('.nav-search .form-control').focus();
	});

	var toggle_sidebar = false,
		toggle_quick_sidebar = false,
		toggle_topbar = false,
		minimize_sidebar = false,
		toggle_page_sidebar = false,
		toggle_overlay_sidebar = false,
		nav_open = 0,
		quick_sidebar_open = 0,
		topbar_open = 0,
		mini_sidebar = 0,
		page_sidebar_open = 0,
		overlay_sidebar_open = 0;


	if (!toggle_sidebar) {
		var toggle = $('.sidenav-toggler');

		toggle.on('click', function () {
			if (nav_open == 1) {
				$('html').removeClass('nav_open');
				toggle.removeClass('toggled');
				nav_open = 0;
			} else {
				$('html').addClass('nav_open');
				toggle.addClass('toggled');
				nav_open = 1;
			}
		});
		toggle_sidebar = true;
	}

	if (!quick_sidebar_open) {
		var toggle = $('.quick-sidebar-toggler');

		toggle.on('click', function () {
			if (nav_open == 1) {
				$('html').removeClass('quick_sidebar_open');
				$('.quick-sidebar-overlay').remove();
				toggle.removeClass('toggled');
				quick_sidebar_open = 0;
			} else {
				$('html').addClass('quick_sidebar_open');
				toggle.addClass('toggled');
				$('<div class="quick-sidebar-overlay"></div>').insertAfter('.quick-sidebar');
				quick_sidebar_open = 1;
			}
		});

		$('.wrapper').mouseup(function (e) {
			var subject = $('.quick-sidebar');

			if (e.target.className != subject.attr('class') && !subject.has(e.target).length) {
				$('html').removeClass('quick_sidebar_open');
				$('.quick-sidebar-toggler').removeClass('toggled');
				$('.quick-sidebar-overlay').remove();
				quick_sidebar_open = 0;
			}
		});

		$(".close-quick-sidebar").on('click', function () {
			$('html').removeClass('quick_sidebar_open');
			$('.quick-sidebar-toggler').removeClass('toggled');
			$('.quick-sidebar-overlay').remove();
			quick_sidebar_open = 0;
		});

		quick_sidebar_open = true;
	}

	if (!toggle_topbar) {
		var topbar = $('.topbar-toggler');

		topbar.on('click', function () {
			if (topbar_open == 1) {
				$('html').removeClass('topbar_open');
				topbar.removeClass('toggled');
				topbar_open = 0;
			} else {
				$('html').addClass('topbar_open');
				topbar.addClass('toggled');
				topbar_open = 1;
			}
		});
		toggle_topbar = true;
	}

	if (!minimize_sidebar) {
		var minibutton = $('.toggle-sidebar');
		if ($('.wrapper').hasClass('sidebar_minimize')) {
			mini_sidebar = 1;
			minibutton.addClass('toggled');
			minibutton.html('<i class="fas fa-ellipsis-v"></i>');
		}

		minibutton.on('click', function () {
			if (mini_sidebar == 1) {
				$('.wrapper').removeClass('sidebar_minimize');
				minibutton.removeClass('toggled');
				minibutton.html('<i class="fas fa-bars"></i>');
				mini_sidebar = 0;
			} else {
				$('.wrapper').addClass('sidebar_minimize');
				minibutton.addClass('toggled');
				minibutton.html('<i class="fas fa-ellipsis-v"></i>');
				mini_sidebar = 1;
			}
			$(window).resize();
		});
		minimize_sidebar = true;
	}

	if (!toggle_page_sidebar) {
		var pageSidebarToggler = $('.page-sidebar-toggler');

		pageSidebarToggler.on('click', function () {
			if (page_sidebar_open == 1) {
				$('html').removeClass('pagesidebar_open');
				pageSidebarToggler.removeClass('toggled');
				page_sidebar_open = 0;
			} else {
				$('html').addClass('pagesidebar_open');
				pageSidebarToggler.addClass('toggled');
				page_sidebar_open = 1;
			}
		});

		var pageSidebarClose = $('.page-sidebar .back');

		pageSidebarClose.on('click', function () {
			$('html').removeClass('pagesidebar_open');
			pageSidebarToggler.removeClass('toggled');
			page_sidebar_open = 0;
		});

		toggle_page_sidebar = true;
	}

	if (!toggle_overlay_sidebar) {
		var overlaybutton = $('.sidenav-overlay-toggler');
		if ($('.wrapper').hasClass('is-show')) {
			overlay_sidebar_open = 1;
			overlaybutton.addClass('toggled');
			overlaybutton.html('<i class="fas fa-ellipsis-v"></i>');
		}

		overlaybutton.on('click', function () {
			if (overlay_sidebar_open == 1) {
				$('.wrapper').removeClass('is-show');
				overlaybutton.removeClass('toggled');
				overlaybutton.html('<i class="fas fa-bars"></i>');
				overlay_sidebar_open = 0;
			} else {
				$('.wrapper').addClass('is-show');
				overlaybutton.addClass('toggled');
				overlaybutton.html('<i class="fas fa-ellipsis-v"></i>');
				overlay_sidebar_open = 1;
			}
			$(window).resize();
		});
		minimize_sidebar = true;
	}

	$('.sidebar').hover(function () {
		if ($('.wrapper').hasClass('sidebar_minimize')) {
			$('.wrapper').addClass('sidebar_minimize_hover');
		}
	}, function () {
		if ($('.wrapper').hasClass('sidebar_minimize')) {
			$('.wrapper').removeClass('sidebar_minimize_hover');
		}
	});

	// addClass if nav-item click and has subnav

	$(".nav-item a").on('click', (function () {
		if ($(this).parent().find('.collapse').hasClass("show")) {
			$(this).parent().removeClass('submenu');
		} else {
			$(this).parent().addClass('submenu');
		}
	}));

	//Chat Open
	$('.messages-contact .user a').on('click', function () {
		$('.tab-chat').addClass('show-chat')
	});

	$('.messages-wrapper .return').on('click', function () {
		$('.tab-chat').removeClass('show-chat')
	});

	//select all
	$('[data-select="checkbox"]').change(function () {
		var target = $(this).attr('data-target');
		$(target).prop('checked', $(this).prop("checked"));
	})

	//form-group-default active if input focus
	$(".form-group-default .form-control").focus(function () {
		$(this).parent().addClass("active");
	}).blur(function () {
		$(this).parent().removeClass("active");
	})

});

// Input File Image

function readURL(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();

		reader.onload = function (e) {
			$(input).parent('.input-file-image').find('.img-upload-preview').attr('src', e.target.result);
		}

		reader.readAsDataURL(input.files[0]);
	}
}

$('.input-file-image input[type="file"').change(function () {
	readURL(this);
});

// Show Password

function showPassword(button) {
	var inputPassword = $(button).parent().find('input');
	if (inputPassword.attr('type') === "password") {
		inputPassword.attr('type', 'text');
		$(".show-password i").removeClass("far fa-eye");
		$(".show-password i").addClass("far fa-eye-slash");
	} else {
		inputPassword.attr('type', 'password');
		$(".show-password i").removeClass("far fa-eye-slash");
		$(".show-password i").addClass("far fa-eye");
	}
}

$('.show-password').on('click', function () {
	showPassword(this);
})

// Sign In & Sign Up
var containerSignIn = $('.container-login'),
	containerSignUp = $('.container-signup'),
	showSignIn = true,
	showSignUp = false;

function changeContainer() {
	if (showSignIn == true) {
		containerSignIn.css('display', 'block')
	} else {
		containerSignIn.css('display', 'none')
	}

	if (showSignUp == true) {
		containerSignUp.css('display', 'block')
	} else {
		containerSignUp.css('display', 'none')
	}
}

$('#show-signup').on('click', function () {
	showSignUp = true;
	showSignIn = false;
	changeContainer();
})

$('#show-signin').on('click', function () {
	showSignUp = false;
	showSignIn = true;
	changeContainer();
})

changeContainer();

//Input with Floating Label

$('.form-floating-label .form-control').keyup(function () {
	if ($(this).val() !== '') {
		$(this).addClass('filled');
	} else {
		$(this).removeClass('filled');
	}
})

// add icon to sidebar
var iconList = [
	'<i class = "fas fa-home"></i>',
	'<i class="fas fa-user-nurse"></i>',
	'<i class="fas fa-users"></i>',
	'<i class="fas fa-clinic-medical"></i>',
	'<i class="fas fa-capsules"></i>',
	'<i class="fas fa-archive"></i>',
	'<i class="fas fa-file-alt"></i>',
	'<i class="fas fa-database"></i>',
	'<i class="fas fa-notes-medical"></i>',
	'<i class="fas fa-info-circle"></i>',
	'<i class="fas fa-unlock-alt"></i>',
	'<i class="fas fa-sign-out-alt"></i>'
];
var i = 0;
var all = $(".sidebar-content > ul > li > a").map(function () {
	$(this).prepend(iconList[i++]);
});

/* --------------- logo header - navbar header - side bar - background switched color ------------ */
// background switch
$(".bg-switch button").on('click', function () {
	if ($(this).attr("data-color") === "bg1") {
		$(this).attr("data-color", "bg1");
		localStorage.setItem("theme-bg", "bg1");
	} else if ($(this).attr("data-color") === "bg2") {
		$(this).attr("data-color", "bg2");
		localStorage.setItem("theme-bg", "bg2");
	} else if ($(this).attr("data-color") === "bg3") {
		$(this).attr("data-color", "bg3");
		localStorage.setItem("theme-bg", "bg3");
	} else {
		$(this).attr("data-color", "dark");
		localStorage.setItem("theme-bg", "dark");
	}
})

// sidebar switch
$(".sidebar-switch button").on('click', function () {
	if ($(this).attr("data-color") === "white") {
		$(this).attr("data-color", "white");
		localStorage.setItem("theme-sidebar", "white");
	} else if ($(this).attr("data-color") === "dark2") {
		$(this).attr("data-color", "dark2");
		localStorage.setItem("theme-sidebar", "dark2");
	} else {
		$(this).attr("data-color", "dark");
		localStorage.setItem("theme-sidebar", "dark");
	}
})

// navbar switch
$(".navbar-switch button").on('click', function () {
	if ($(this).attr("data-color") === "dark") {
		$(this).attr("data-color", "dark");
		localStorage.setItem("theme-navbar", "dark");

	} else if ($(this).attr("data-color") === "blue") {
		$(this).attr("data-color", "blue");
		localStorage.setItem("theme-navbar", "blue");

	} else if ($(this).attr("data-color") === "purple") {
		$(this).attr("data-color", "purple");
		localStorage.setItem("theme-navbar", "purple");

	} else if ($(this).attr("data-color") === "light-blue") {
		$(this).attr("data-color", "light-blue");
		localStorage.setItem("theme-navbar", "light-blue");

	} else if ($(this).attr("data-color") === "green") {
		$(this).attr("data-color", "green");
		localStorage.setItem("theme-navbar", "green");

	} else if ($(this).attr("data-color") === "orange") {
		$(this).attr("data-color", "orange");
		localStorage.setItem("theme-navbar", "orange");

	} else if ($(this).attr("data-color") === "red") {
		$(this).attr("data-color", "red");
		localStorage.setItem("theme-navbar", "red");

	} else if ($(this).attr("data-color") === "white") {
		$(this).attr("data-color", "white");
		localStorage.setItem("theme-navbar", "white");

	} else if ($(this).attr("data-color") === "dark2") {
		$(this).attr("data-color", "dark2");
		localStorage.setItem("theme-navbar", "dark2");

	} else if ($(this).attr("data-color") === "blue2") {
		$(this).attr("data-color", "blue2");
		localStorage.setItem("theme-navbar", "blue2");

	} else if ($(this).attr("data-color") === "purple2") {
		$(this).attr("data-color", "purple2");
		localStorage.setItem("theme-navbar", "purple2");

	} else if ($(this).attr("data-color") === "light-blue2") {
		$(this).attr("data-color", "light-blue2");
		localStorage.setItem("theme-navbar", "light-blue2");

	} else if ($(this).attr("data-color") === "green2") {
		$(this).attr("data-color", "green2");
		localStorage.setItem("theme-navbar", "green2");

	} else if ($(this).attr("data-color") === "orange2") {
		$(this).attr("data-color", "orange2");
		localStorage.setItem("theme-navbar", "orange2");

	} else {
		$(this).attr("data-color", "red2");
		localStorage.setItem("theme-navbar", "red2");
	}
})

// logo switch
$(".logo-switch button").on('click', function () {
	if ($(this).attr("data-color") === "dark") {
		$(this).attr("data-color", "dark");
		localStorage.setItem("theme-logo", "dark");

	} else if ($(this).attr("data-color") === "blue") {
		$(this).attr("data-color", "blue");
		localStorage.setItem("theme-logo", "blue");

	} else if ($(this).attr("data-color") === "purple") {
		$(this).attr("data-color", "purple");
		localStorage.setItem("theme-logo", "purple");

	} else if ($(this).attr("data-color") === "light-blue") {
		$(this).attr("data-color", "light-blue");
		localStorage.setItem("theme-logo", "light-blue");

	} else if ($(this).attr("data-color") === "green") {
		$(this).attr("data-color", "green");
		localStorage.setItem("theme-logo", "green");

	} else if ($(this).attr("data-color") === "orange") {
		$(this).attr("data-color", "orange");
		localStorage.setItem("theme-logo", "orange");

	} else if ($(this).attr("data-color") === "red") {
		$(this).attr("data-color", "red");
		localStorage.setItem("theme-logo", "red");

	} else if ($(this).attr("data-color") === "white") {
		$(this).attr("data-color", "white");
		localStorage.setItem("theme-logo", "white");

	} else if ($(this).attr("data-color") === "dark2") {
		$(this).attr("data-color", "dark2");
		localStorage.setItem("theme-logo", "dark2");

	} else if ($(this).attr("data-color") === "blue2") {
		$(this).attr("data-color", "blue2");
		localStorage.setItem("theme-logo", "blue2");

	} else if ($(this).attr("data-color") === "purple2") {
		$(this).attr("data-color", "purple2");
		localStorage.setItem("theme-logo", "purple2");

	} else if ($(this).attr("data-color") === "light-blue2") {
		$(this).attr("data-color", "light-blue2");
		localStorage.setItem("theme-logo", "light-blue2");

	} else if ($(this).attr("data-color") === "green2") {
		$(this).attr("data-color", "green2");
		localStorage.setItem("theme-logo", "green2");

	} else if ($(this).attr("data-color") === "orange2") {
		$(this).attr("data-color", "orange2");
		localStorage.setItem("theme-logo", "orange2");

	} else {
		$(this).attr("data-color", "red2");
		localStorage.setItem("theme-logo", "red2");
	}
})

function themeMode() {
	// checking if 'theme-bg' key exists
	if (localStorage.getItem("theme-bg") !== null) {
		if (localStorage.getItem("theme-bg") === "bg1") {
			$("body").attr("data-background-color", "bg1");
		} else if (localStorage.getItem("theme-bg") === "bg2") {
			$("body").attr("data-background-color", "bg2");
		} else if (localStorage.getItem("theme-bg") === "bg3") {
			$("body").attr("data-background-color", "bg3");
		} else {
			$("body").attr("data-background-color", "dark");
		}
	}

	// checking if 'theme-sidebar' key exists
	if (localStorage.getItem("theme-sidebar") !== null) {
		if (localStorage.getItem("theme-sidebar") === "white") {
			$(".sidebar").attr("data-background-color", "white");
		} else if (localStorage.getItem("theme-sidebar") === "dark") {
			$(".sidebar").attr("data-background-color", "dark");
		} else {
			$(".sidebar").attr("data-background-color", "dark2");
		}
	}

	// checking if 'theme-navbar' key exists
	if (localStorage.getItem("theme-navbar") !== null) {
		if (localStorage.getItem("theme-navbar") === "dark") {
			$(".navbar-header").attr("data-background-color", "dark");
		} else if (localStorage.getItem("theme-navbar") === "blue") {
			$(".navbar-header").attr("data-background-color", "blue");
		} else if (localStorage.getItem("theme-navbar") === "purple") {
			$(".navbar-header").attr("data-background-color", "purple");
		} else if (localStorage.getItem("theme-navbar") === "light-blue") {
			$(".navbar-header").attr("data-background-color", "light-blue");
		} else if (localStorage.getItem("theme-navbar") === "green") {
			$(".navbar-header").attr("data-background-color", "green");
		} else if (localStorage.getItem("theme-navbar") === "orange") {
			$(".navbar-header").attr("data-background-color", "orange");
		} else if (localStorage.getItem("theme-navbar") === "red") {
			$(".navbar-header").attr("data-background-color", "red");
		} else if (localStorage.getItem("theme-navbar") === "white") {
			$(".navbar-header").attr("data-background-color", "white");
		} else if (localStorage.getItem("theme-navbar") === "dark2") {
			$(".navbar-header").attr("data-background-color", "dark2");
		} else if (localStorage.getItem("theme-navbar") === "blue2") {
			$(".navbar-header").attr("data-background-color", "blue2");
		} else if (localStorage.getItem("theme-navbar") === "purple2") {
			$(".navbar-header").attr("data-background-color", "purple2");
		} else if (localStorage.getItem("theme-navbar") === "light-blue2") {
			$(".navbar-header").attr("data-background-color", "light-blue2");
		} else if (localStorage.getItem("theme-navbar") === "green2") {
			$(".navbar-header").attr("data-background-color", "green2");
		} else if (localStorage.getItem("theme-navbar") === "orange2") {
			$(".navbar-header").attr("data-background-color", "orange2");
		} else {
			$(".navbar-header").attr("data-background-color", "red2");
		}
	}

	// checking if 'theme-logo' key exists
	if (localStorage.getItem("theme-logo") !== null) {
		if (localStorage.getItem("theme-logo") === "dark") {
			$(".logo-header").attr("data-background-color", "dark");
		} else if (localStorage.getItem("theme-logo") === "blue") {
			$(".logo-header").attr("data-background-color", "blue");
		} else if (localStorage.getItem("theme-logo") === "purple") {
			$(".logo-header").attr("data-background-color", "purple");
		} else if (localStorage.getItem("theme-logo") === "light-blue") {
			$(".logo-header").attr("data-background-color", "light-blue");
		} else if (localStorage.getItem("theme-logo") === "green") {
			$(".logo-header").attr("data-background-color", "green");
		} else if (localStorage.getItem("theme-logo") === "orange") {
			$(".logo-header").attr("data-background-color", "orange");
		} else if (localStorage.getItem("theme-logo") === "red") {
			$(".logo-header").attr("data-background-color", "red");
		} else if (localStorage.getItem("theme-logo") === "white") {
			$(".logo-header").attr("data-background-color", "white");
		} else if (localStorage.getItem("theme-logo") === "dark2") {
			$(".logo-header").attr("data-background-color", "dark2");
		} else if (localStorage.getItem("theme-logo") === "blue2") {
			$(".logo-header").attr("data-background-color", "blue2");
		} else if (localStorage.getItem("theme-logo") === "purple2") {
			$(".logo-header").attr("data-background-color", "purple2");
		} else if (localStorage.getItem("theme-logo") === "light-blue2") {
			$(".logo-header").attr("data-background-color", "light-blue2");
		} else if (localStorage.getItem("theme-logo") === "green2") {
			$(".logo-header").attr("data-background-color", "green2");
		} else if (localStorage.getItem("theme-logo") === "orange2") {
			$(".logo-header").attr("data-background-color", "orange2");
		} else {
			$(".logo-header").attr("data-background-color", "red2");
		}
	}
}
themeMode();