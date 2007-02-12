Summary:	SELinux policy generation scripts and tools
Summary(pl.UTF-8):   Skrypty i narzędzia do generowania polityk SELinuksa
Name:		polgen
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/polgen/%{name}-%{version}.tar.gz
# Source0-md5:	81c53ecf7d7f3901c3f3778708f267fa
Patch0:		%{name}-info.patch
URL:		http://polgen.sourceforge.net/
BuildRequires:	flex
BuildRequires:	libselinux-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	texinfo
%pyrequires_eq	python-libs
# contains SELinux-enhanced version of strace
Obsoletes:	strace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polgen is a collection of scripts and tools developed by the MITRE
corporation to automate the SELinux policy generation process.

%description -l pl.UTF-8
polgen to zestaw skryptów i narzędzi stworzonych przez firmę MITRE w
celu zautomatyzowania procesu generowania polityk SELinuksa.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/polgen.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}
%{_mandir}/man[18]/*
%{_infodir}/*.info*
