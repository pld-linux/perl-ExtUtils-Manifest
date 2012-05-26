#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	Manifest
Summary:	ExtUtils::Manifest - utilities to write and check a MANIFEST file
Summary(pl.UTF-8):	ExtUtils::Manifest - narzędzia do tworzenia i sprawdzania plików MANIFEST
Name:		perl-ExtUtils-Manifest
Version:	1.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0146485d2f730a3676d0058cd4bbdd02
URL:		http://search.cpan.org/dist/ExtUtils-Manifest/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::Manifest contains the functions to write and check MANIFEST
files.

%description -l pl.UTF-8
Moduł ExtUtils::Manifest zawiera funkcje do zapisu i sprawdzania
plików MANIFEST.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Manifest.pm
%{perl_vendorlib}/ExtUtils/MANIFEST.SKIP
%{_mandir}/man3/ExtUtils::Manifest.3pm*
