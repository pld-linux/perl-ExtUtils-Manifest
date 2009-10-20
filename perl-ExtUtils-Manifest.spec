#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	Manifest
Summary:	ExtUtils::Manifest - utilities to write and check a MANIFEST file
Name:		perl-ExtUtils-Manifest
Version:	1.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a606c372a9800d7403f1c856a63d814
URL:		http://search.cpan.org/dist/ExtUtils-Manifest/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::Manifest exports no functions by default. The following are
exported on request

A list of files in the distribution, one file per line. The MANIFEST
always uses Unix filepath conventions even if you're not on Unix. This
means foo/bar style not foo\bar.

Anything between white space and an end of line within a MANIFEST file
is considered to be a comment. Any line beginning with # is also a
comment. Beginning with ExtUtils::Manifest 1.52, a filename may
contain whitespace characters if it is enclosed in single quotes;
single quotes or backslashes in that filename must be
backslash-escaped.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/*.pm
%{_mandir}/man3/*
