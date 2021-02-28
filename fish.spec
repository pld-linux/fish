Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eba358c6c99e596b8633113ff1cd5994
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

%package devel
Summary:	Development files for fish
Summary(pl.UTF-8):	Pliki programistyczne dla fish
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description devel
Development files for fish.

%description devel -l pl.UTF-8
Pliki programistyczne dla fish.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python},' share/tools/{deroff.py,create_manpage_completions.py,web_config/webconfig.py}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure

%{__make} V=1

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
%dir %{_sysconfdir}/fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish/config.fish
%attr(755,root,root) %{_bindir}/fish
%attr(755,root,root) %{_bindir}/fish_indent
%attr(755,root,root) %{_bindir}/fish_key_reader
%{_mandir}/man1/fish.1*
%{_mandir}/man1/fish_indent.1*
%{_mandir}/man1/fish_key_reader.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config.fish
%{_datadir}/%{name}/__fish_build_paths.fish
%dir %{_datadir}/%{name}/completions
%{_datadir}/%{name}/completions/*.fish
%dir %{_datadir}/%{name}/groff
%{_datadir}/%{name}/groff/fish.tmac
%{_datadir}/%{name}/vendor_completions.d
%dir %{_datadir}/%{name}/functions
%{_datadir}/%{name}/functions/*.fish
%{_datadir}/%{name}/lynx.lss
%{_datadir}/%{name}/man
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/create_manpage_completions.py
%{_datadir}/%{name}/tools/deroff.py
%dir %{_datadir}/%{name}/tools/web_config
%{_datadir}/%{name}/tools/web_config/delete.png
%{_datadir}/%{name}/tools/web_config/favicon.png
%{_datadir}/%{name}/tools/web_config/fishconfig.css
%{_datadir}/%{name}/tools/web_config/index.html
%{_datadir}/%{name}/tools/web_config/js
%{_datadir}/%{name}/tools/web_config/partials
%{_datadir}/%{name}/tools/web_config/sample_prompts
%attr(755,root,root) %{_datadir}/%{name}/tools/web_config/webconfig.py

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/fish.pc
