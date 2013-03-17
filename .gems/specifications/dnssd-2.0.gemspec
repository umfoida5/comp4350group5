# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{dnssd}
  s.version = "2.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Eric Hodel", "Aaron Patterson", "Phil Hagelberg", "Chad Fowler", "Charles Mills", "Rich Kilmer"]
  s.cert_chain = ["-----BEGIN CERTIFICATE-----\nMIIDNjCCAh6gAwIBAgIBADANBgkqhkiG9w0BAQUFADBBMRAwDgYDVQQDDAdkcmJy\nYWluMRgwFgYKCZImiZPyLGQBGRYIc2VnbWVudDcxEzARBgoJkiaJk/IsZAEZFgNu\nZXQwHhcNMDcxMjIxMDIwNDE0WhcNMDgxMjIwMDIwNDE0WjBBMRAwDgYDVQQDDAdk\ncmJyYWluMRgwFgYKCZImiZPyLGQBGRYIc2VnbWVudDcxEzARBgoJkiaJk/IsZAEZ\nFgNuZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCbbgLrGLGIDE76\nLV/cvxdEzCuYuS3oG9PrSZnuDweySUfdp/so0cDq+j8bqy6OzZSw07gdjwFMSd6J\nU5ddZCVywn5nnAQ+Ui7jMW54CYt5/H6f2US6U0hQOjJR6cpfiymgxGdfyTiVcvTm\nGj/okWrQl0NjYOYBpDi+9PPmaH2RmLJu0dB/NylsDnW5j6yN1BEI8MfJRR+HRKZY\nmUtgzBwF1V4KIZQ8EuL6I/nHVu07i6IkrpAgxpXUfdJQJi0oZAqXurAV3yTxkFwd\ng62YrrW26mDe+pZBzR6bpLE+PmXCzz7UxUq3AE0gPHbiMXie3EFE0oxnsU3lIduh\nsCANiQ8BAgMBAAGjOTA3MAkGA1UdEwQCMAAwCwYDVR0PBAQDAgSwMB0GA1UdDgQW\nBBS5k4Z75VSpdM0AclG2UvzFA/VW5DANBgkqhkiG9w0BAQUFAAOCAQEAHagT4lfX\nkP/hDaiwGct7XPuVGbrOsKRVD59FF5kETBxEc9UQ1clKWngf8JoVuEoKD774dW19\nbU0GOVWO+J6FMmT/Cp7nuFJ79egMf/gy4gfUfQMuvfcr6DvZUPIs9P/TlK59iMYF\nDIOQ3DxdF3rMzztNUCizN4taVscEsjCcgW6WkUJnGdqlu3OHWpQxZBJkBTjPCoc6\nUW6on70SFPmAy/5Cq0OJNGEWBfgD9q7rrs/X8GGwUWqXb85RXnUVi/P8Up75E0ag\n14jEc90kN+C7oI/AGCBN0j6JnEtYIEJZibjjDJTSMWlUKKkj30kq7hlUC2CepJ4v\nx52qPcexcYZR7w==\n-----END CERTIFICATE-----\n"]
  s.date = %q{2011-03-03}
  s.description = %q{DNS Service Discovery (aka Bonjour, MDNS) API for Ruby.  Implements browsing,
resolving, registration and domain enumeration.  Supports avahi's DNSSD
compatibility layer for avahi 0.6.25 or newer.}
  s.email = ["drbrain@segment.net", "aaronp@rubyforge.org", "phil@hagelb.org", "chad@chadfowler.com", "", ""]
  s.extensions = ["ext/dnssd/extconf.rb"]
  s.extra_rdoc_files = ["History.txt", "Manifest.txt", "README.txt"]
  s.files = [".autotest", "History.txt", "Manifest.txt", "README.txt", "Rakefile", "ext/dnssd/dnssd.c", "ext/dnssd/dnssd.h", "ext/dnssd/errors.c", "ext/dnssd/extconf.rb", "ext/dnssd/flags.c", "ext/dnssd/record.c", "ext/dnssd/service.c", "lib/dnssd.rb", "lib/dnssd/flags.rb", "lib/dnssd/record.rb", "lib/dnssd/reply.rb", "lib/dnssd/reply/addr_info.rb", "lib/dnssd/reply/browse.rb", "lib/dnssd/reply/domain.rb", "lib/dnssd/reply/query_record.rb", "lib/dnssd/reply/register.rb", "lib/dnssd/reply/resolve.rb", "lib/dnssd/service.rb", "lib/dnssd/text_record.rb", "sample/browse.rb", "sample/enumerate_domains.rb", "sample/getaddrinfo.rb", "sample/growl.rb", "sample/query_record.rb", "sample/register.rb", "sample/resolve.rb", "sample/resolve_ichat.rb", "sample/server.rb", "sample/socket.rb", "test/test_dnssd.rb", "test/test_dnssd_flags.rb", "test/test_dnssd_record.rb", "test/test_dnssd_reply.rb", "test/test_dnssd_reply_browse.rb", "test/test_dnssd_reply_query_record.rb", "test/test_dnssd_reply_resolve.rb", "test/test_dnssd_service.rb", "test/test_dnssd_text_record.rb", ".gemtest"]
  s.homepage = %q{http://rubyforge.org/projects/dnssd}
  s.rdoc_options = ["--main", "README.txt"]
  s.require_paths = ["lib"]
  s.rubyforge_project = %q{dnssd}
  s.rubygems_version = %q{1.3.6}
  s.summary = %q{DNS Service Discovery (aka Bonjour, MDNS) API for Ruby}
  s.test_files = ["test/test_dnssd.rb", "test/test_dnssd_flags.rb", "test/test_dnssd_record.rb", "test/test_dnssd_reply.rb", "test/test_dnssd_reply_browse.rb", "test/test_dnssd_reply_query_record.rb", "test/test_dnssd_reply_resolve.rb", "test/test_dnssd_service.rb", "test/test_dnssd_text_record.rb"]

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 3

    if Gem::Version.new(Gem::RubyGemsVersion) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<minitest>, [">= 2.0.2"])
      s.add_development_dependency(%q<rake-compiler>, ["~> 0.7"])
      s.add_development_dependency(%q<hoe>, [">= 2.9.0"])
    else
      s.add_dependency(%q<minitest>, [">= 2.0.2"])
      s.add_dependency(%q<rake-compiler>, ["~> 0.7"])
      s.add_dependency(%q<hoe>, [">= 2.9.0"])
    end
  else
    s.add_dependency(%q<minitest>, [">= 2.0.2"])
    s.add_dependency(%q<rake-compiler>, ["~> 0.7"])
    s.add_dependency(%q<hoe>, [">= 2.9.0"])
  end
end
