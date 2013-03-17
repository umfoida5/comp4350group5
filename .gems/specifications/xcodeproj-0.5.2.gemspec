# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{xcodeproj}
  s.version = "0.5.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Eloy Duran"]
  s.date = %q{2013-03-09}
  s.default_executable = %q{xcodeproj}
  s.description = %q{Xcodeproj lets you create and modify Xcode projects from Ruby. Script boring management tasks or build Xcode-friendly libraries. Also includes support for Xcode workspaces (.xcworkspace) and configuration files (.xcconfig).}
  s.email = %q{eloy.de.enige@gmail.com}
  s.executables = ["xcodeproj"]
  s.extensions = ["ext/xcodeproj/extconf.rb"]
  s.files = ["lib/xcodeproj/command/project_diff.rb", "lib/xcodeproj/command/show.rb", "lib/xcodeproj/command/target_diff.rb", "lib/xcodeproj/command.rb", "lib/xcodeproj/config.rb", "lib/xcodeproj/constants.rb", "lib/xcodeproj/differ.rb", "lib/xcodeproj/helper.rb", "lib/xcodeproj/project/object/build_configuration.rb", "lib/xcodeproj/project/object/build_file.rb", "lib/xcodeproj/project/object/build_phase.rb", "lib/xcodeproj/project/object/build_rule.rb", "lib/xcodeproj/project/object/configuration_list.rb", "lib/xcodeproj/project/object/container_item_proxy.rb", "lib/xcodeproj/project/object/file_reference.rb", "lib/xcodeproj/project/object/group.rb", "lib/xcodeproj/project/object/native_target.rb", "lib/xcodeproj/project/object/reference_proxy.rb", "lib/xcodeproj/project/object/root_object.rb", "lib/xcodeproj/project/object/target_dependency.rb", "lib/xcodeproj/project/object.rb", "lib/xcodeproj/project/object_attributes.rb", "lib/xcodeproj/project/object_dictionary.rb", "lib/xcodeproj/project/object_list.rb", "lib/xcodeproj/project.rb", "lib/xcodeproj/user_interface.rb", "lib/xcodeproj/workspace.rb", "lib/xcodeproj.rb", "ext/xcodeproj/extconf.rb", "ext/xcodeproj/xcodeproj_ext.c", "README.md", "LICENSE", "bin/xcodeproj"]
  s.homepage = %q{https://github.com/cocoapods/xcodeproj}
  s.licenses = ["MIT"]
  s.require_paths = ["ext", "lib"]
  s.rubygems_version = %q{1.3.6}
  s.summary = %q{Create and modify Xcode projects from Ruby.}

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 3

    if Gem::Version.new(Gem::RubyGemsVersion) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<activesupport>, ["~> 3.2.6"])
      s.add_runtime_dependency(%q<colored>, ["~> 1.2"])
    else
      s.add_dependency(%q<activesupport>, ["~> 3.2.6"])
      s.add_dependency(%q<colored>, ["~> 1.2"])
    end
  else
    s.add_dependency(%q<activesupport>, ["~> 3.2.6"])
    s.add_dependency(%q<colored>, ["~> 1.2"])
  end
end
