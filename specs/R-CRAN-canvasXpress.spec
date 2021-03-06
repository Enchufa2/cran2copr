%global packname  canvasXpress
%global packver   1.29.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.29.6
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization Package for CanvasXpress in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-stats 
Requires:         R-CRAN-htmlwidgets >= 1.0
Requires:         R-CRAN-httr 
Requires:         R-stats 

%description
Enables creation of visualizations using the CanvasXpress framework in R.
CanvasXpress is a standalone JavaScript library for reproducible research
with complete tracking of data and end-user modifications stored in a
single PNG image that can be played back. See
<https://www.canvasxpress.org> for more information.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
