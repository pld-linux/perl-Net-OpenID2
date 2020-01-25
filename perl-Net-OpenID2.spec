#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	OpenID2
Summary:	OpenID 2.0 library
Summary(pl.UTF-8):	Implementacja standardu OpenID 2.0
Name:		perl-Net-OpenID2
Version:	0.9.0.2
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://code.sxip.com/downloads/perl-openid-sxip-%{version}.tar.gz
# Source0-md5:	a8f159d7853e206303e30a8753614dbe
URL:		http://code.sxip.com/openid4perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Crypt-DH
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Net-Yadis
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Libaries for:
- OpenID Authentication 2.0
- OpenID Attribute Exchange 1.0

%description -l pl.UTF-8
Biblioteka Perla implementująca:
- OpenID Authentication 2.0
- OpenID Attribute Exchange 1.0

%prep
%setup -q -n perl-openid-sxip-%{version}

%build
AUTOMATED_TESTING=1
export AUTOMATED_TESTING
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
%doc INSTALL README
%{perl_vendorlib}/Net/OpenID2/
%{_mandir}/man3/*
