Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	1.23.0
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://www.fishshell.org/files/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aa2f09bb54652b16bf4f7708848a7416
Patch0:		%{name}-link.patch
URL:		http://fishshell.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
Requires:	man-whatis
Suggests:	xsel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%description -l pl.UTF-8
fish jest powłoką nastawioną na interaktywne używanie. Jego cechą jest
przyjazne nastawienie dla użytkownika. Składnia języka jest prosta ale
nie jest zgodna z innymi językami powłoki.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%{__autoheader}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--docdir=/docs \
	--without-xsel
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT/docs docs

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README docs/*.{html,css,png}
%attr(755,root,root) %{_bindir}/fish*
%attr(755,root,root) %{_bindir}/mimedb
%attr(755,root,root) %{_bindir}/set_color
%{_datadir}/%{name}
%dir %{_sysconfdir}/fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish/config.fish
%{_mandir}/man1/fish*.1*
%{_mandir}/man1/mimedb.1*
%{_mandir}/man1/set_color.1*
