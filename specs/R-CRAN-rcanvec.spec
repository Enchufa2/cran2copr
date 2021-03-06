%global packname  rcanvec
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Plot CanVec and CanVec+ Data for Rapid Basemap Creation in Canada

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 

%description
Provides an interface to the National Topographic System (NTS), which is
the way in which a number of freely available Canadian datasets are
organized. CanVec and CanVec+ datasets, which include all data used to
create Canadian topographic maps, are two such datasets that are useful in
creating vector-based maps for locations across Canada. This packages
searches CanVec data by location, plots it using pretty defaults, and
exports it to human- readable shapefiles for use in another GIS.

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
