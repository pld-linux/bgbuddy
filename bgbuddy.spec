%include	/usr/lib/rpm/macros.perl
Summary:	Automatic wallpaper rotating daemon
Summary(pl.UTF-8):	Demon służący do automatycznej zmiany tapety
Name:		bgbuddy
Version:	1.22
Release:	1
License:	QPL
Group:		Daemons
Source0:	http://www.fewt.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	221004eabce6e1c1f5a0deaf6dad0c23
URL:		http://www.fewt.com/bgbuddy.shtml
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatic wallpaper rotating daemon. It supports GNOME 2.x,
WindowMaker, FluxBox and XFCE.

%description -l pl.UTF-8
Demon służący do automatycznej zmiany tapety. Działa z GNOME 2.x,
WindowMakerem, FluxBoksem, i XFCE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog license.txt readme
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
