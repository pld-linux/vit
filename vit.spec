Summary:	Lightweight, fast, curses-based front end to Taskwarrior
Name:		vit
Version:	2.3.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/vit-project/vit/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	149b8e9aa2b0c919b0007e319d03ff66
URL:		https://github.com/vit-project/vit/releases
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.720
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visual Interactive Taskwarrior full-screen terminal interface includes
following features:

- Fully-customizable key bindings (default Vim-like)
- Uncluttered display
- No mouse
- Speed
- Per-column colorization
- Advanced tab completion
- Multiple/customizable themes
- Override/customize column formatters
- Intelligent sub-project indenting

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,CHANGES,COLOR,CUSTOMIZE,DEVELOPMENT,FAQ,README,UPGRADE}.md
%attr(755,root,root) %{_bindir}/vit
%{py3_sitescriptdir}/vit
%{py3_sitescriptdir}/vit-%{version}-py3*.egg-info
