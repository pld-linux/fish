Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	2.2.0
Release:	2
License:	GPL v2
Group:		Applications/Shells
Source0:	http://fishshell.com/files/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f6c3d940148593ff6648adb07986cbcb
URL:		http://fishshell.com/
BuildRequires:	autoconf >= 2.60
BuildRequires:	doxygen
BuildRequires:	gettext-tools
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.462
Suggests:	python
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

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%lua_add_etc_shells %{_bindir}/fish

%preun -p <lua>
if arg[2] == 0 then
	%lua_remove_etc_shells %{_bindir}/fish
end

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md user_doc/html/*.{html,css,png}
%attr(755,root,root) %{_bindir}/fish*
%attr(755,root,root) %{_bindir}/mimedb
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config.fish
%dir %{_datadir}/%{name}/completions
%{_datadir}/%{name}/completions/..fish
%{_datadir}/%{name}/completions/*.fish
%{_datadir}/%{name}/vendor_completions.d
%dir %{_datadir}/%{name}/functions
%{_datadir}/%{name}/functions/*.fish
%{_datadir}/%{name}/man
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/create_manpage_completions.py
%{_datadir}/%{name}/tools/deroff.py
%dir %{_datadir}/%{name}/tools/web_config
%{_datadir}/%{name}/tools/web_config/delete.png
%{_datadir}/%{name}/tools/web_config/fishconfig.css
%{_datadir}/%{name}/tools/web_config/index.html
%{_datadir}/%{name}/tools/web_config/js
%{_datadir}/%{name}/tools/web_config/partials
%{_datadir}/%{name}/tools/web_config/sample_prompts
%attr(755,root,root) %{_datadir}/%{name}/tools/web_config/webconfig.py
%dir %{_sysconfdir}/fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish/config.fish
%{_mandir}/man1/fish*.1*
%{_mandir}/man1/mimedb.1*
