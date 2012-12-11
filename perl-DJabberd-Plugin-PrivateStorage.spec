%define realname   DJabberd-Plugin-PrivateStorage

Name:		perl-%{realname}
Version:	0.60
Release:	4
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Implement private storage, as described in XEP-0049, for DJabberd
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DJabberd/DJabberd-Plugin-PrivateStorage-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}

BuildRequires:	perl-devel
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(DBD::SQLite) 
BuildRequires:	perl(DJabberd)
BuildArch:	noarch

%description
Implement private storage, as described in XEP-0049, for DJabberd.

This is used by various jabber client to store room bookmark, or notes
on contact in the roster.
 
%prep
%setup -q -n DJabberd-Plugin-PrivateStorage-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled until they work again
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/DJabberd/
%{_mandir}/man3/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.60-3mdv2011.0
+ Revision: 681365
- mass rebuild

* Sun Nov 22 2009 Michael Scherer <misc@mandriva.org> 0.60-2mdv2011.0
+ Revision: 469114
- disable test as they requires to be rewritten
- fix BuildRequires
- import perl-DJabberd-Plugin-PrivateStorage

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 20 2007 Michael Scherer <misc@mandriva.org> 0.60-1mdv2008.0
- First Mandriva package
