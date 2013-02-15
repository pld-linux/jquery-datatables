%define		plugin	datatables
Summary:	DataTables (table plug-in for jQuery)
Name:		jquery-%{plugin}
Version:	1.9.4
Release:	1
License:	GPL v2, BSD
Group:		Applications/WWW
Source0:	http://www.datatables.net/releases/DataTables-%{version}.zip
# Source0-md5:	136f9ce380015161a6543cc17221908c
URL:		http://www.datatables.net/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jquery >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
DataTables is a plug-in for the jQuery JavaScript library. It is a
highly flexible tool, based upon the foundations of progressive
enhancement, which will add advanced interaction controls to any HTML
table.

%prep
%setup -qn DataTables-%{version}

%{__sed} -i -e 's,../images/,,' media/css/*.css
%{__rm} media/images/*.psd
%{__rm} media/images/*.ico

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p media/js/jquery.dataTables.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p media/js/jquery.dataTables.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p media/css/jquery.dataTables.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

cp -a media/images/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.txt
%{_appdir}
