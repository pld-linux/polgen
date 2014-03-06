Summary:	SELinux policy generation scripts and tools
Summary(pl.UTF-8):	Skrypty i narzędzia do generowania polityk SELinuksa
Name:		polgen
Version:	2.0
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/polgen/%{name}-%{version}.tar.gz
# Source0-md5:	ff3124ab7b1acc6a6854e9c377d3f981
Patch0:		%{name}-info.patch
Patch1:		%{name}-python.patch
URL:		http://polgen.sourceforge.net/
BuildRequires:	audit-libs-devel
BuildRequires:	flex
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	texinfo
%pyrequires_eq	python-libs
Requires:	python-audit
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
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/polgen.html
%attr(755,root,root) %{_bindir}/aulogsort
%attr(755,root,root) %{_bindir}/auptrace
%attr(755,root,root) %{_bindir}/autrackfd
%attr(755,root,root) %{_bindir}/ecomm-config
%attr(755,root,root) %{_bindir}/spar
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}
%{_infodir}/polgen.info*
