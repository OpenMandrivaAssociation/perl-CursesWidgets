%define upstream_name    CursesWidgets
%define upstream_version 1.997

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Assorted widgets for rapid interface design
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Curses)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


