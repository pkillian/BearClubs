var BearClubs = BearClubs || {};

(function(that, $, window, document, undefined) {
    "use strict";

    // false == 60 >= scrollTop > 0
    // true  == scrollTop > 60
    this.scrolled = false;
    this.mousedOver = false;
    this.headerShown = true;
    this.headerHeight = 60;
    this.photoScrollers = {};

    this.bindHeaderMouseOver = function(ev) {
        that.mousedOver = (ev.clientY <= that.headerHeight + 20);

        // If the page is scrolled, the header isn't shown, and the mouse is between 0-80...
        if (that.scrolled && !that.headerShown && that.mousedOver) {

            // Show the header!
            that.toggleHeader(true);

        // If the page is scrolled, the header is shown, and the mouse is between 81-inf...
        } else if (that.scrolled && that.headerShown && !that.mousedOver) {

            // Hide the header
            that.toggleHeader(false);
        }
    };

    this.bindHeaderScroll = function(ev) {
        that.scrolled = ($(window).scrollTop() > that.headerHeight);

        if (that.mousedOver) {
            return false;
        }

        // If not scrolled past the header already, and the window scrolls past the header...
        if (that.headerShown && that.scrolled) {

            // Hide the header!
            that.toggleHeader(false);

        // If scrolled past the header already, and the window has scrolled above the header...
        } else if (!that.headerShown && !that.scrolled) {

            // Show the header!
            that.toggleHeader(true);

        }
    };

    this.toggleHeader = function (toggle) {
        if (toggle) {
            // Show the header
            $('#header').animate({height: that.headerHeight + 'px'}, 'fast', function() {
                $('#header').css('border-bottom-style', 'solid');
            });
        } else {
            // Hide the header
            $('#header').animate({height: '0px'}, 'fast', function() {
                $('#header').css('border-bottom-style', 'none');
            });
        }

        that.headerShown = toggle;
    };

    $.fn.styleTable = function (options) {
        var defaults = {
            css: 'styleTable'
        };

        options = $.extend(defaults, options);

        return this.each(function () {

            var input = $(this);
            input.addClass(options.css);

            input.find("tr").on('mouseover mouseout', function (event) {
                if (event.type === 'mouseover') {
                    $(this).children("td").addClass("ui-state-hover");
                } else {
                    $(this).children("td").removeClass("ui-state-hover");
                }
            });

            input.find("th").addClass("ui-state-default");
            input.find("td").addClass("ui-widget-content");

            input.find("tr").each(function () {
                $(this).children("td:not(:first)").addClass("first");
                $(this).children("th:not(:first)").addClass("first");
            });
        });
    };

    this.onReady = function() {
        $(window).scroll(that.bindHeaderScroll);
        $(window).mousemove(that.bindHeaderMouseOver);
        $('#club-directory').styleTable();
        $('#club-directory').tablesorter({widgets: ['zebra']});
    };

}).call(BearClubs, BearClubs, jQuery, window, document);
