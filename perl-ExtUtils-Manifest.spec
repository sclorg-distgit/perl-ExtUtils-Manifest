%{?scl:%scl_package perl-ExtUtils-Manifest}

Name:           %{?scl_prefix}perl-ExtUtils-Manifest
Version:        1.70
Release:        366%{?dist}
Summary:        Utilities to write and check a MANIFEST file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-Manifest/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/ExtUtils-Manifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
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
# VMS::Feature not used
# VMS::Filespec not used
# Tests:
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# CPAN::Meta not needed
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(File::Path)

%description
%{summary}.

%prep
%setup -q -n ExtUtils-Manifest-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.70-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-2
- Perl 5.22 rebuild

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 1.70-1
- 1.70 bump

* Thu Nov 20 2014 Petr Pisar <ppisar@redhat.com> - 1.69-1
- 1.69 bump

* Wed Sep 17 2014 Petr Pisar <ppisar@redhat.com> - 1.68-1
- 1.68 bump

* Wed Sep 10 2014 Petr Pisar <ppisar@redhat.com> - 1.66-1
- 1.66 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-2
- Perl 5.20 rebuild

* Tue Aug 12 2014 Petr Pisar <ppisar@redhat.com> - 1.65-1
- 1.65 bump

* Tue Jul 29 2014 Petr Pisar <ppisar@redhat.com> - 1.64-1
- 1.64 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-245
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.61-244
- Perl 5.18 rebuild

* Tue Apr 30 2013 Petr Pisar <ppisar@redhat.com> - 1.61-243
- Increase release number to supersede perl sub-package (bug #957931)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-241
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Petr Pisar <ppisar@redhat.com> - 1.61-240
- Increase release to remove sub-package from perl

* Thu Sep 13 2012 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.60-2
- Perl 5.16 rebuild

* Mon Nov 28 2011 Petr Pisar <ppisar@redhat.com> 1.60-1
- Specfile autogenerated by cpanspec 1.78.
- Remove defattr and BuildRoot from spec code.
