%define upstream_name    CursesWidgets
%define upstream_version 1.997

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Assorted widgets for rapid interface design
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Curses)
BuildArch:	noarch

%description
This module serves two purposes: to provide a framework for creating custom
widget classes, and importing a few useful functions for global use.

Widget specific methods are documented in each Widget's pod.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests require human input
#make test

%install
%makeinstall_std

%files
%doc CHANGELOG LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.997.0-2mdv2011.0
+ Revision: 658523
- rebuild for updated spec-helper

* Wed Jun 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.997.0-1mdv2011.0
+ Revision: 547324
- import perl-CursesWidgets


* Wed Jun 09 2010 cpan2dist 1.997-1mdv
- initial mdv release, generated with cpan2dist
