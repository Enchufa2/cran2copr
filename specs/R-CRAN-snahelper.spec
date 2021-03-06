%global packname  snahelper
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Addin for Network Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggraph >= 2.0.0
BuildRequires:    R-CRAN-graphlayouts >= 0.5.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-ggraph >= 2.0.0
Requires:         R-CRAN-graphlayouts >= 0.5.0
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-DT 

%description
'RStudio' addin which provides a GUI to visualize and analyse networks.
After finishing a session, the code to produce the plot is inserted in the
current script. Alternatively, the function SNAhelperGadget() can be used
directly from the console. Additional addins include the Netreader() for
reading network files, Netbuilder() to create small networks via point and
click, and the Componentlayouter() to layout networks with many components
manually.

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
