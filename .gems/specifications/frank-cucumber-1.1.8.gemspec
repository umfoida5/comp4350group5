# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{frank-cucumber}
  s.version = "1.1.8"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Pete Hodgson", "Derek Longmuir"]
  s.date = %q{2013-02-08}
  s.description = %q{Use cucumber to test native iOS apps via Frank}
  s.email = ["gems@thepete.net"]
  s.executables = ["frank", "frank-skeleton"]
  s.files = [".gitignore", "Gemfile", "Rakefile", "bin/frank", "bin/frank-skeleton", "frank-cucumber.gemspec", "frank-skeleton/features/my_first.feature", "frank-skeleton/features/step_definitions/launch_steps.rb", "frank-skeleton/features/support/env.rb", "frank-skeleton/frankify.xcconfig.tt", "frank-skeleton/libCocoaAsyncSocket.a", "frank-skeleton/libCocoaAsyncSocketMac.a", "frank-skeleton/libCocoaHTTPServer.a", "frank-skeleton/libCocoaHTTPServerMac.a", "frank-skeleton/libCocoaLumberjack.a", "frank-skeleton/libCocoaLumberjackMac.a", "frank-skeleton/libFrank.a", "frank-skeleton/libFrankMac.a", "frank-skeleton/libShelley.a", "frank-skeleton/libShelleyMac.a", "lib/frank-cucumber.rb", "lib/frank-cucumber/app_bundle_locator.rb", "lib/frank-cucumber/bonjour.rb", "lib/frank-cucumber/cli.rb", "lib/frank-cucumber/color_helper.rb", "lib/frank-cucumber/console.rb", "lib/frank-cucumber/core_frank_steps.rb", "lib/frank-cucumber/frank_helper.rb", "lib/frank-cucumber/frank_localize.rb", "lib/frank-cucumber/frank_mac_helper.rb", "lib/frank-cucumber/frankifier.rb", "lib/frank-cucumber/gateway.rb", "lib/frank-cucumber/gesture_helper.rb", "lib/frank-cucumber/host_scripting.rb", "lib/frank-cucumber/keyboard_helper.rb", "lib/frank-cucumber/launcher.rb", "lib/frank-cucumber/localize.yml", "lib/frank-cucumber/location_helper.rb", "lib/frank-cucumber/mac_launcher.rb", "lib/frank-cucumber/rect.rb", "lib/frank-cucumber/scroll_helper.rb", "lib/frank-cucumber/version.rb", "lib/frank-cucumber/wait_helper.rb", "test/keyboard_helper_test.rb", "test/launcher_test.rb", "test/rect_test.rb", "test/test_helper.rb", "frank-skeleton/frank_static_resources.bundle/images/ajax-loader.gif", "frank-skeleton/frank_static_resources.bundle/images/file.gif", "frank-skeleton/frank_static_resources.bundle/images/folder-closed.gif", "frank-skeleton/frank_static_resources.bundle/images/folder.gif", "frank-skeleton/frank_static_resources.bundle/images/loader.gif", "frank-skeleton/frank_static_resources.bundle/images/loader.png", "frank-skeleton/frank_static_resources.bundle/images/minus.gif", "frank-skeleton/frank_static_resources.bundle/images/plus.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-black-line.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-black.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-default-line.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-default.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-famfamfam-line.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-famfamfam.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-gray-line.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-gray.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-red-line.gif", "frank-skeleton/frank_static_resources.bundle/images/treeview-red.gif", "frank-skeleton/frank_static_resources.bundle/index.html", "frank-skeleton/frank_static_resources.bundle/index.html.haml", "frank-skeleton/frank_static_resources.bundle/js/accessible_views_view.coffee", "frank-skeleton/frank_static_resources.bundle/js/accessible_views_view.js", "frank-skeleton/frank_static_resources.bundle/js/controller.coffee", "frank-skeleton/frank_static_resources.bundle/js/controller.js", "frank-skeleton/frank_static_resources.bundle/js/details_view.coffee", "frank-skeleton/frank_static_resources.bundle/js/details_view.js", "frank-skeleton/frank_static_resources.bundle/js/dropdown_control.coffee", "frank-skeleton/frank_static_resources.bundle/js/dropdown_control.js", "frank-skeleton/frank_static_resources.bundle/js/ersatz_model.coffee", "frank-skeleton/frank_static_resources.bundle/js/ersatz_model.js", "frank-skeleton/frank_static_resources.bundle/js/ersatz_view.coffee", "frank-skeleton/frank_static_resources.bundle/js/ersatz_view.js", "frank-skeleton/frank_static_resources.bundle/js/experiment_bar_model.coffee", "frank-skeleton/frank_static_resources.bundle/js/experiment_bar_model.js", "frank-skeleton/frank_static_resources.bundle/js/experiment_bar_view.coffee", "frank-skeleton/frank_static_resources.bundle/js/experiment_bar_view.js", "frank-skeleton/frank_static_resources.bundle/js/frank.coffee", "frank-skeleton/frank_static_resources.bundle/js/frank.js", "frank-skeleton/frank_static_resources.bundle/js/lib/backbone.js", "frank-skeleton/frank_static_resources.bundle/js/lib/coffee-script.js", "frank-skeleton/frank_static_resources.bundle/js/lib/jquery-ui.min.js", "frank-skeleton/frank_static_resources.bundle/js/lib/jquery.min.js", "frank-skeleton/frank_static_resources.bundle/js/lib/jquery.treeview.js", "frank-skeleton/frank_static_resources.bundle/js/lib/json2.js", "frank-skeleton/frank_static_resources.bundle/js/lib/raphael.js", "frank-skeleton/frank_static_resources.bundle/js/lib/require.js", "frank-skeleton/frank_static_resources.bundle/js/lib/underscore.js", "frank-skeleton/frank_static_resources.bundle/js/main.coffee", "frank-skeleton/frank_static_resources.bundle/js/main.js", "frank-skeleton/frank_static_resources.bundle/js/tabs_controller.coffee", "frank-skeleton/frank_static_resources.bundle/js/tabs_controller.js", "frank-skeleton/frank_static_resources.bundle/js/toast_controller.coffee", "frank-skeleton/frank_static_resources.bundle/js/toast_controller.js", "frank-skeleton/frank_static_resources.bundle/js/transform_stack.coffee", "frank-skeleton/frank_static_resources.bundle/js/transform_stack.js", "frank-skeleton/frank_static_resources.bundle/js/tree_view.coffee", "frank-skeleton/frank_static_resources.bundle/js/tree_view.js", "frank-skeleton/frank_static_resources.bundle/js/view_hier_model.coffee", "frank-skeleton/frank_static_resources.bundle/js/view_hier_model.js", "frank-skeleton/frank_static_resources.bundle/js/view_model.coffee", "frank-skeleton/frank_static_resources.bundle/js/view_model.js", "frank-skeleton/frank_static_resources.bundle/pictos/index.html", "frank-skeleton/frank_static_resources.bundle/pictos/pictos-web.eot", "frank-skeleton/frank_static_resources.bundle/pictos/pictos-web.svg", "frank-skeleton/frank_static_resources.bundle/pictos/pictos-web.ttf", "frank-skeleton/frank_static_resources.bundle/pictos/pictos-web.woff", "frank-skeleton/frank_static_resources.bundle/pictos/pictos.css", "frank-skeleton/frank_static_resources.bundle/pictos/pictos_base64.css", "frank-skeleton/frank_static_resources.bundle/stylesheets/css/symbiote.css", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_elements.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_header.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_inspect_tabs_list_tabs.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_jquery.treeview.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_jqui.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_layout.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_mixins.sass", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_reset.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_selector_test_toolbar.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_solarized.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_typography.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_unicode.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/_z_index.scss", "frank-skeleton/frank_static_resources.bundle/stylesheets/sass/symbiote.scss", "frank-skeleton/frank_static_resources.bundle/ViewAttributeMapping.plist", "frank-skeleton/frank_static_resources.bundle/ViewAttributeMappingMac.plist"]
  s.homepage = %q{http://rubygems.org/gems/frank-cucumber}
  s.require_paths = ["lib"]
  s.rubygems_version = %q{1.3.6}
  s.summary = %q{Use cucumber to test native iOS apps via Frank}
  s.test_files = ["test/keyboard_helper_test.rb", "test/launcher_test.rb", "test/rect_test.rb", "test/test_helper.rb"]

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 3

    if Gem::Version.new(Gem::RubyGemsVersion) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<cucumber>, [">= 0"])
      s.add_runtime_dependency(%q<rspec>, [">= 2.0"])
      s.add_runtime_dependency(%q<sim_launcher>, [">= 0.4.6"])
      s.add_runtime_dependency(%q<i18n>, [">= 0"])
      s.add_runtime_dependency(%q<plist>, [">= 0"])
      s.add_runtime_dependency(%q<json>, [">= 0"])
      s.add_runtime_dependency(%q<dnssd>, [">= 0"])
      s.add_runtime_dependency(%q<thor>, [">= 0"])
      s.add_runtime_dependency(%q<xcodeproj>, [">= 0"])
      s.add_development_dependency(%q<rr>, [">= 0"])
      s.add_development_dependency(%q<yard>, [">= 0"])
      s.add_development_dependency(%q<pry>, [">= 0"])
      s.add_development_dependency(%q<pry-debugger>, [">= 0"])
    else
      s.add_dependency(%q<cucumber>, [">= 0"])
      s.add_dependency(%q<rspec>, [">= 2.0"])
      s.add_dependency(%q<sim_launcher>, [">= 0.4.6"])
      s.add_dependency(%q<i18n>, [">= 0"])
      s.add_dependency(%q<plist>, [">= 0"])
      s.add_dependency(%q<json>, [">= 0"])
      s.add_dependency(%q<dnssd>, [">= 0"])
      s.add_dependency(%q<thor>, [">= 0"])
      s.add_dependency(%q<xcodeproj>, [">= 0"])
      s.add_dependency(%q<rr>, [">= 0"])
      s.add_dependency(%q<yard>, [">= 0"])
      s.add_dependency(%q<pry>, [">= 0"])
      s.add_dependency(%q<pry-debugger>, [">= 0"])
    end
  else
    s.add_dependency(%q<cucumber>, [">= 0"])
    s.add_dependency(%q<rspec>, [">= 2.0"])
    s.add_dependency(%q<sim_launcher>, [">= 0.4.6"])
    s.add_dependency(%q<i18n>, [">= 0"])
    s.add_dependency(%q<plist>, [">= 0"])
    s.add_dependency(%q<json>, [">= 0"])
    s.add_dependency(%q<dnssd>, [">= 0"])
    s.add_dependency(%q<thor>, [">= 0"])
    s.add_dependency(%q<xcodeproj>, [">= 0"])
    s.add_dependency(%q<rr>, [">= 0"])
    s.add_dependency(%q<yard>, [">= 0"])
    s.add_dependency(%q<pry>, [">= 0"])
    s.add_dependency(%q<pry-debugger>, [">= 0"])
  end
end
