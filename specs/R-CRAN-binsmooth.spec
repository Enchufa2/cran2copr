%global packname  binsmooth
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Generate PDFs and CDFs from Binned Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-triangle 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-triangle 

%description
Provides several methods for generating density functions based on binned
data. Methods include step function, recursive subdivision, and optimized
spline. Data are assumed to be nonnegative, but the bin widths need not be
equal, and the top bin need not have an upper bound. All PDF smoothing
methods maintain the areas specified by the binned data. (Equivalently,
all CDF smoothing methods interpolate the points specified by the binned
data.) An estimate for the mean of the distribution may be supplied as an
optional argument, which greatly improves the reliability of statistics
computed from the smoothed density functions. Includes methods for
estimating the Gini coefficient, the Theil index, percentiles, and random
deviates from a smoothed distribution. Among the three methods, the
optimized spline (splinebins) is recommended for most purposes. The
percentile and random-draw functions only support splinebins.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX