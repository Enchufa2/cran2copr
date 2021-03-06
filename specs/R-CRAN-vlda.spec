%global packname  vlda
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          2%{?dist}%{?buildtag}
Summary:          Visualization of Multidimensional Longitudinal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggsci 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggsci 

%description
Assists in producing a plot that more effectively expresses changes over
time for two different types (long format and wide format) using a
consistent calling scheme for longitudinal data. It provides the ability
to projection supplementary information (supplementary objects and
variables) that can often occur in longitudinal data to graphs, as well as
provides a new interactive implementation to perform the additional
interpretation, so it is also useful for longitudinal data visuals
analysis (see
<http://lib.pusan.ac.kr/resource/e-article/?app=eds&mod=detail&record_id=edsker.000004649097&db_id=edsker>
for more information).

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
