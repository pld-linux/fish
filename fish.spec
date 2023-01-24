Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	3.3.1
Release:	4
License:	GPL v2
Group:		Applications/Shells
Source0:	https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	94be285255aadfcf0f910bdcc2f56073
Patch0:		%{name}-no_lld.patch
Patch1:		%{name}-rel_datadir.patch
URL:		http://fishshell.com/
BuildRequires:	cmake >= 3.2
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	ncurses-devel
BuildRequires:	pcre2-32-devel >= 10.21
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	pcre2-32 >= 10.21
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
BuildArch:	noarch

%description devel
Development files for fish.

%description devel -l pl.UTF-8
Pliki programistyczne dla fish.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python},' share/tools/{deroff.py,create_manpage_completions.py,web_config/webconfig.py}

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

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
%doc CHANGELOG.rst CONTRIBUTING.rst README.rst user_doc/html/{*.html,*.js,cmds,_static}
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
%dir %{_datadir}/%{name}/vendor_completions.d
%dir %{_datadir}/%{name}/vendor_conf.d
%dir %{_datadir}/%{name}/vendor_functions.d

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/fish.pc
