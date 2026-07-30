%define upstream_name    CursesWidgets
%define upstream_version 1.997

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Assorted widgets for rapid interface design
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/CursesWidgets
Source0:	https://cpan.metacpan.org/authors/id/C/CO/CORLISS/CursesWidgets-1.997.tar.gz

BuildRequires:	make
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

