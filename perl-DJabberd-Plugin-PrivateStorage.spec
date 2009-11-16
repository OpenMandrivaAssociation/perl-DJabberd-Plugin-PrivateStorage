%define realname   DJabberd-Plugin-PrivateStorage

Name:		perl-%{realname}
Version:    0.60
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Implement private storage, as described in XEP-0049, for DJabberd
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/DJabberd/DJabberd-Plugin-PrivateStorage-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires: perl(File::Slurp)
BuildRequires: perl(DBD::SQLite) 
BuildRequires: perl(DJabberd)
BuildArch: noarch

%description
Implement private storage, as described in XEP-0049, for DJabberd.

This is used by various jabber client to store room bookmark, or notes
on contact in the roster.
 
%prep
%setup -q -n DJabberd-Plugin-PrivateStorage-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DJabberd/
%{_mandir}/man3/*

