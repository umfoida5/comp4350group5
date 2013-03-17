
SHELL = /bin/sh

#### Start of system configuration section. ####

srcdir = .
topdir = /System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/lib/ruby/1.8/universal-darwin12.0
hdrdir = $(topdir)
VPATH = $(srcdir):$(topdir):$(hdrdir)
exec_prefix = $(prefix)
prefix = $(DESTDIR)/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr
libexecdir = $(exec_prefix)/libexec
vendorlibdir = $(vendordir)/$(ruby_version)
sysconfdir = $(prefix)/etc
rubylibdir = $(libdir)/ruby/$(ruby_version)
datadir = $(datarootdir)
sitelibdir = $(sitedir)/$(ruby_version)
sharedstatedir = $(prefix)/com
libdir = $(exec_prefix)/lib
infodir = $(DESTDIR)/usr/share/info
oldincludedir = $(DESTDIR)/usr/include
datarootdir = $(prefix)/share
localstatedir = $(prefix)/var
archdir = $(rubylibdir)/$(arch)
htmldir = $(docdir)
sitearchdir = $(sitelibdir)/$(sitearch)
dvidir = $(docdir)
sbindir = $(exec_prefix)/sbin
docdir = $(datarootdir)/doc/$(PACKAGE)
vendorarchdir = $(vendorlibdir)/$(sitearch)
psdir = $(docdir)
bindir = $(exec_prefix)/bin
sitedir = $(DESTDIR)/Library/Ruby/Site
vendordir = $(libdir)/ruby/vendor_ruby
pdfdir = $(docdir)
mandir = $(DESTDIR)/usr/share/man
localedir = $(datarootdir)/locale
includedir = $(prefix)/include

CC = xcrun cc
LIBRUBY = $(LIBRUBY_SO)
LIBRUBY_A = lib$(RUBY_SO_NAME)-static.a
LIBRUBYARG_SHARED = -l$(RUBY_SO_NAME)
LIBRUBYARG_STATIC = -l$(RUBY_SO_NAME)

RUBY_EXTCONF_H = 
CFLAGS   =  -fno-common -arch i386 -arch x86_64 -g -Os -pipe -fno-common -DENABLE_DTRACE  -fno-common  -pipe -fno-common $(cflags) 
INCFLAGS = -I. -I. -I/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/lib/ruby/1.8/universal-darwin12.0 -I.
DEFS     = 
CPPFLAGS = -DHAVE_DNS_SD_H -DHAVE_IF_INDEXTONAME -DHAVE_IF_NAMETOINDEX -DHAVE_GETSERVBYPORT -DHAVE_TYPE_STRUCT_SOCKADDR_IN -DHAVE_ST_SIN_LEN -DHAVE_DNSSERVICEGETPROPERTY -DHAVE_DNSSERVICEGETADDRINFO -DHAVE_KDNSSERVICEFLAGSFORCE -DHAVE_KDNSSERVICEFLAGSNONBROWSABLE -DHAVE_KDNSSERVICEFLAGSRETURNINTERMEDIATES -DHAVE_KDNSSERVICEFLAGSSHARECONNECTION -DHAVE_KDNSSERVICEERR_BADSIG  -D_XOPEN_SOURCE -D_DARWIN_C_SOURCE  
CXXFLAGS = $(CFLAGS) 
ldflags  = -L. -arch i386 -arch x86_64 
dldflags = 
archflag = 
DLDFLAGS = $(ldflags) $(dldflags) $(archflag)
LDSHARED = cc -arch i386 -arch x86_64 -pipe -bundle -undefined dynamic_lookup
AR = ar
EXEEXT = 

RUBY_INSTALL_NAME = ruby
RUBY_SO_NAME = ruby
arch = universal-darwin12.0
sitearch = universal-darwin12.0
ruby_version = 1.8
ruby = /System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby
RUBY = $(ruby)
RM = rm -f
MAKEDIRS = mkdir -p
INSTALL = /usr/bin/install -c
INSTALL_PROG = $(INSTALL) -m 0755
INSTALL_DATA = $(INSTALL) -m 644
COPY = cp

#### End of system configuration section. ####

preload = 

libpath = . $(libdir)
LIBPATH =  -L. -L$(libdir)
DEFFILE = 

CLEANFILES = mkmf.log
DISTCLEANFILES = 

extout = 
extout_prefix = 
target_prefix = /dnssd
LOCAL_LIBS = 
LIBS = $(LIBRUBYARG_SHARED) -lSystem  -lpthread -ldl -lobjc  
SRCS = service.c record.c errors.c dnssd.c flags.c
OBJS = service.o record.o errors.o dnssd.o flags.o
TARGET = dnssd
DLLIB = $(TARGET).bundle
EXTSTATIC = 
STATIC_LIB = 

BINDIR        = $(bindir)
RUBYCOMMONDIR = $(sitedir)$(target_prefix)
RUBYLIBDIR = /home/student/umlatkap/Desktop/comp4350group5/.gems/gems/dnssd-2.0/lib$(target_prefix)
RUBYARCHDIR = /home/student/umlatkap/Desktop/comp4350group5/.gems/gems/dnssd-2.0/lib$(target_prefix)

TARGET_SO     = $(DLLIB)
CLEANLIBS     = $(TARGET).bundle $(TARGET).il? $(TARGET).tds $(TARGET).map
CLEANOBJS     = *.o *.a *.s[ol] *.pdb *.exp *.bak

all:		$(DLLIB)
static:		$(STATIC_LIB)

clean:
		@-$(RM) $(CLEANLIBS) $(CLEANOBJS) $(CLEANFILES)

distclean:	clean
		@-$(RM) Makefile $(RUBY_EXTCONF_H) conftest.* mkmf.log
		@-$(RM) core ruby$(EXEEXT) *~ $(DISTCLEANFILES)

realclean:	distclean
install: install-so install-rb

install-so: $(RUBYARCHDIR)
install-so: $(RUBYARCHDIR)/$(DLLIB)
$(RUBYARCHDIR)/$(DLLIB): $(DLLIB)
	$(INSTALL_PROG) $(DLLIB) $(RUBYARCHDIR)
install-rb: pre-install-rb install-rb-default
install-rb-default: pre-install-rb-default
pre-install-rb: Makefile
pre-install-rb-default: Makefile
$(RUBYARCHDIR):
	$(MAKEDIRS) $@

site-install: site-install-so site-install-rb
site-install-so: install-so
site-install-rb: install-rb

.SUFFIXES: .c .m .cc .cxx .cpp .C .o

.cc.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.cxx.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.cpp.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.C.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.c.o:
	$(CC) $(INCFLAGS) $(CPPFLAGS) $(CFLAGS) -c $<

$(DLLIB): $(OBJS) Makefile
	@-$(RM) $@
	$(LDSHARED) -o $@ $(OBJS) $(LIBPATH) $(DLDFLAGS) $(LOCAL_LIBS) $(LIBS)



$(OBJS): ruby.h defines.h
