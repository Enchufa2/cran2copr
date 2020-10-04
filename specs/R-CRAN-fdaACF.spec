%global packname  fdaACF
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Autocorrelation Function for Functional Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-fda 
Requires:         R-Matrix 
Requires:         R-CRAN-vars 

%description
Quantify the serial correlation across lags of a given functional time
series using an autocorrelation function and a partial autocorrelation
function for functional time series. The autocorrelation functions are
based on the L2 norm of the lagged covariance operators of the series.
Functions are available for estimating the distribution of the
autocorrelation functions under the assumption of strong functional white
noise.

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
