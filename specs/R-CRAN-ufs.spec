%global packname  ufs
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Quantitative Analysis Made Accessible

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-SuppDists >= 1.1.9
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-diptest >= 0.75.7
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-pander >= 0.6.3
BuildRequires:    R-CRAN-digest >= 0.6.19
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-ggridges >= 0.5.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
Requires:         R-grDevices >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-SuppDists >= 1.1.9
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-diptest >= 0.75.7
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-pander >= 0.6.3
Requires:         R-CRAN-digest >= 0.6.19
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-ggridges >= 0.5.0
Requires:         R-CRAN-gtable >= 0.2.0

%description
This is a new version of the 'userfriendlyscience' package, which has
grown a bit unwieldy. Therefore, distinct functionalities are being
'consciously uncoupled' into different packages. This package contains the
general-purpose tools and utilities (see the 'behaviorchange' package, the
'rosetta' package, and the soon-to-be-released 'scd' package for other
functionality), and is the most direct 'successor' of the original
'userfriendlyscience' package. For example, this package contains a number
of basic functions to create higher level plots, such as diamond plots, to
easily plot sampling distributions, to generate confidence intervals, to
plan study sample sizes for confidence intervals, and to do some basic
operations such as (dis)attenuate effect size estimates.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/partials
%{rlibdir}/%{packname}/INDEX
