%{?scl:%scl_package perl-ExtUtils-Manifest}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-ExtUtils-Manifest
Version:        1.63
Release:        2.sc1%{?dist}
Summary:        Utilities to write and check a MANIFEST file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-Manifest/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/ExtUtils-Manifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(vars)
# VMS::Feature not used
# VMS::Filespec not used
# Tests:
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(File::Path)
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.8

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(File::Spec\\)\\s*$

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(File::Spec)\s*$/d
%filter_setup
%endif

%description
%{summary}.

%prep
%setup -q -n ExtUtils-Manifest-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-2
- Updated conditions to work properly for non-RHEL systems
- Resolves: rhbz#1064855

* Tue Nov 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-1
- 1.63 bump

* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-100
- Stack package - initial release
