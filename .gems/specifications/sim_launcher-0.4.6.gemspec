# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{sim_launcher}
  s.version = "0.4.6"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Pete Hodgson"]
  s.date = %q{2012-10-01}
  s.default_executable = %q{sim_launcher}
  s.email = ["rubygems@thepete.net"]
  s.executables = ["sim_launcher"]
  s.files = [".gitignore", ".gitmodules", "Gemfile", "Rakefile", "bin/sim_launcher", "lib/sim_launcher.rb", "lib/sim_launcher/client.rb", "lib/sim_launcher/direct_client.rb", "lib/sim_launcher/sdk_detector.rb", "lib/sim_launcher/simulator.rb", "lib/sim_launcher/version.rb", "native/ios-sim", "native/iphonesim", "sim_launcher.gemspec"]
  s.homepage = %q{http://rubygems.org/gems/sim_launcher}
  s.require_paths = ["lib"]
  s.rubygems_version = %q{1.3.6}
  s.summary = %q{tiny HTTP server to launch an app in the iOS simulator}

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 3

    if Gem::Version.new(Gem::RubyGemsVersion) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<sinatra>, [">= 0"])
    else
      s.add_dependency(%q<sinatra>, [">= 0"])
    end
  else
    s.add_dependency(%q<sinatra>, [">= 0"])
  end
end
