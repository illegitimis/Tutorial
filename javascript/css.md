# CSS

## Todo

- design steal 8164.org [1]
- StackOverflow team [2]
- Sass: Mixin or Placeholder? [3]
- simplelineicons [4] preview
- node-sass vs sass-loader [5]
- _Responsive Websites With Bootstrap 3_ by Mark Zamoyta Pluralsight course page [6] _Jan 2015_. Learn to create a modern, responsive website using Bootstrap 3.
- _CSS3 In-Depth_ by Estelle Weyl Pluralsight course page [7] _Feb 2013_
- Modern Web Layout with Flexbox and CSS Grid Pluralsight course page [8] by Brian Treese, _Jan 2016_. Explore the modern world of web layout with the Flexible Box Module and CSS Grid Layout.
- _CSS3 In-Depth_ by Estelle Weyl Pluralsight course page [7] _Feb 2013_
- Responsive In-Browser Web Page Design with HTML and CSS Pluralsight course page [9] by Karen Menezes, _Sep 2015_. In this HTML and CSS tutorial, we'll learn how to create a responsive site from scratch by prototyping directly in the browser.
- CSS **Grid** Layout (aka "Grid"). Complete Guide to Grid [10]
- estelle/CSS-Workshop [11] 6 hours workshop covering almost everything in CSS2 and CSS3 with demo [12] and _CSS3 In-Depth_ CSS3 In-Depth Pluralsight course page [7], css selectors demo [13]. jQuery & CSS3 Selectors [14] article. slides [15].
- [select[ivizr]](http://selectivizr.com/) is a JavaScript utility that emulates CSS3 pseudo-classes and attribute selectors in Internet Explorer 6-8.
- `::after` pseudo-element mdn [16]
- quackit.com: Html Fieldset Tag.Cfm [17]
- `text-align` qk [18]
- `text-align-last` qk [19]
- quackit.com: Css Text Align.Cfm [20]
- `line-height` qk [21], fun [22]
- `nth-child` pseudo-selector tester [23], std [24]
- Polyfills. _A shim that mimics a future API providing fallback functionality to older browsers._ HTML5 Cross Browser [25]. Regressive Enhancement.

## Bootstrap

- **mobile-first**, wroblewski site [26] and online book [27]
- _Bootstrap 4_ overview [28] and samples [29]
- _Responsive Websites With Bootstrap 3_ by Mark Zamoyta Pluralsight course page [6] _Jan 2015_. Learn to create a modern, responsive website using Bootstrap 3.
- my Bootstrap3 grid sample [30] on codepen
- Multi-Device Layout Patterns [31] March, 2012. by Luke Wroblewski
  - _Mostly Fluid_: multi-column layout, stacks columns vertically
  - _Column drop_: starts with a multi-column layout and ends up with a single column layout, dropping columns along the way as screen sizes get narrower. Unlike the Mostly Fluid pattern, the overall size of elements in this layout tend to stay consistent. Adapting to various screen sizes instead relies on stacking columns
  - _Layout Shifter_: does the most to adapt across different screen sizes. That is, different layouts are used on large, medium, and small screens. Because this inherently requires more work, it seems to be less popular than the previous two patterns. This is where a lot of innovative design is happening.
  - _Content Reflow_: change display characteritics of individual elements depending on viewport characteristics (media queries)
  - Tiny Tweaks
  - Off Canvas
- add the responsive viewport meta tag [32] to your `<head>`.
- List of glyph icons [33], v3.2.2
- _Navigation bar_
  - Supported content [34] like  `.navbar-nav`
  - navbar forms sample [35]
  - A fixed header [36] that will animate its size on scroll. ngx2 [37].
  - navigation bar is hidden on small screens and replaced by a button [38]  in the top right corner. bootstrap 3.3.7 and jquery 1.9
  - fixed to top [39] with bootstrap 4 and jquery 3.

## Flexbox

- Modern Web Layout with Flexbox and CSS Grid Pluralsight course page [8] by Brian Treese, _Jan 2016_. Explore the modern world of web layout with the Flexible Box Module and CSS Grid Layout.
- Quick guide to flexbox [40]

## Almanac

- `list-style` * [41]
- media queries [42] on MDN

[1]: http://www.8164.org/
[2]: https://stackoverflow.com/company/team
[3]: https://www.sitepoint.com/sass-mixin-placeholder/
[4]: http://simplelineicons.com/
[5]: https://stackoverflow.com/questions/33310216/scss-loader-with-webpack
[6]: https://app.pluralsight.com/library/courses/responsive-websites-bootstrap3/table-of-contents
[7]: https://app.pluralsight.com/library/courses/css3-in-depth/table-of-contents
[8]: https://app.pluralsight.com/library/courses/modern-web-layout-flexbox-css-grid/table-of-contents
[9]: https://app.pluralsight.com/library/courses/responsive-browser-web-page-design-html-css-2262/table-of-contents
[10]: https://css-tricks.com/snippets/css/complete-guide-grid/
[11]: https://github.com/estelle/CSS-Workshop
[12]: http://www.standardista.com/webstock/
[13]: https://estelle.github.io/cssmastery/selectors
[14]: http://standardista.com/jquery/
[15]: https://estelle.github.io/cssmastery/selectors/#slide1
[16]: https://developer.mozilla.org/en-US/docs/Web/CSS/::after
[17]: https://www.quackit.com/html_5/tags/html_fieldset_tag.cfm
[18]: https://www.quackit.com/css/css3/properties/css_text-align.cfm
[19]: https://www.quackit.com/css/css3/properties/css_text-align-last.cfm
[20]: https://www.quackit.com/css/properties/css_text-align.cfm
[21]: https://www.quackit.com/css/properties/css_line-height.cfm
[22]: https://css-tricks.com/fun-line-height/
[23]: https://css-tricks.com/examples/nth-child-tester/
[24]: http://standardista.com/jquery/#slcNthOfTypes
[25]: https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-browser-Polyfills
[26]: http://static.lukew.com/MobileFirst_LukeW.pdf
[27]: http://www.ferrispark.com/audio/DOCUMENTS/mobile-first.pdf
[28]: http://getbootstrap.com/docs/4.0/layout/overview/
[29]: http://getbootstrap.com/docs/4.0/examples/
[30]: https://codepen.io/illegitimis/pen/zzwvRv
[31]: https://www.lukew.com/ff/entry.asp?1514
[32]: http://getbootstrap.com/docs/4.0/getting-started/introduction/#responsive-meta-tag
[33]: http://glyphicons.bootstrapcheatsheets.com/
[34]: https://getbootstrap.com/docs/4.0/components/navbar/#supported-content
[35]: http://v4-alpha.getbootstrap.com/components/navbar/#forms
[36]: https://github.com/codrops/AnimatedHeader
[37]: https://github.com/mvanbeusekom/Angular-2---Animated-Header
[38]: https://codepen.io/JohnnyBizzel/pen/QGEapj
[39]: https://codepen.io/mmekaiel/pen/ZOPKKR
[40]: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
[41]: https://css-tricks.com/almanac/properties/l/list-style/
[42]: https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries

[<<](./index.md) | [home](../README.md)
