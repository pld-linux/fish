Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	4.0.6
Release:	0.2
License:	GPL v2
Group:		Applications/Shells
Source0:	https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	33abf3cfaa592a43b4823b8ff46d5246
Source1:	vendor.tar.zst
# Source1-md5:	4524ed43b1e3c069077cb21f9da627b8
URL:		http://fishshell.com/
BuildRequires:	cargo
BuildRequires:	cmake >= 3.15
BuildRequires:	gettext-tools
BuildRequires:	pcre2-32-devel >= 10.21
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.020
BuildRequires:	rust
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	terminfo
BuildRequires:	xz
Requires:	pcre2-32 >= 10.21
Requires:       awk
Requires:       bc
Requires:       gzip
Requires:       man
Suggests:	python3
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
%setup -q -a1

%{__sed} -i -e '1s,/usr/bin/env python3$,%{__python3},' share/tools/create_manpage_completions.py

%build
%cmake -B build \
	-DRust_COMPILER:PATH="%{__rustc}" \
	-DRust_CARGO:PATH="%{__cargo}" \
	-DRust_CARGO_TARGET="%{rust_target}" \
	-DCARGO_FLAGS:LIST="%(printf '%s' '%__cargo_common_opts --release' | tr '[[:space:]]' ';')" \
	-DFISH_USE_SYSTEM_PCRE2:BOOL=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{set_build_flags};
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
%{_mandir}/man1/fish-completions.1*
%{_mandir}/man1/fish-doc.1*
%{_mandir}/man1/fish-faq.1*
%{_mandir}/man1/fish-for-bash-users.1*
%{_mandir}/man1/fish-interactive.1*
%{_mandir}/man1/fish-language.1*
%{_mandir}/man1/fish-prompt-tutorial.1*
%{_mandir}/man1/fish-tutorial.1*
%{_mandir}/man1/fish.1*
%{_mandir}/man1/fish_indent.1*
%{_mandir}/man1/fish_key_reader.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config.fish
%{_datadir}/%{name}/__fish_build_paths.fish
%dir %{_datadir}/%{name}/completions
%{_datadir}/%{name}/completions/*.fish
%{_datadir}/fish/completions/..fish
%dir %{_datadir}/%{name}/groff
%{_datadir}/%{name}/groff/fish.tmac
%dir %{_datadir}/%{name}/functions
%{_datadir}/%{name}/functions/*.fish
%{_datadir}/%{name}/man
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/create_manpage_completions.py
%{_datadir}/%{name}/tools/deroff.py
%dir %{_datadir}/%{name}/tools/web_config
%{_datadir}/%{name}/tools/web_config/favicon.png
%{_datadir}/%{name}/tools/web_config/fishconfig.css
%{_datadir}/%{name}/tools/web_config/fishconfig_print.css
%{_datadir}/%{name}/tools/web_config/index.html
%{_datadir}/%{name}/tools/web_config/js
%{_datadir}/%{name}/tools/web_config/sample_prompts
%{_datadir}/%{name}/tools/web_config/themes
%{_desktopdir}/fish.desktop
%{_pixmapsdir}/fish.png
%attr(755,root,root) %{_datadir}/%{name}/tools/web_config/webconfig.py
%dir %{_datadir}/%{name}/vendor_completions.d
%dir %{_datadir}/%{name}/vendor_conf.d
%dir %{_datadir}/%{name}/vendor_functions.d

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/fish.pc
