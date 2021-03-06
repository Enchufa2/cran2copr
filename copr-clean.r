#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

if (!interactive())
  stop("please, run this interactively and think deeply about what you're doing")

df.mon <- get_monitor()
latest <- unique(unname(sapply(strsplit(unlist(df.mon[,-1]), " "), "[", 1)))

df.builds <- get_builds()
df.rm <- subset(df.builds, !`Build ID` %in% latest)

message("Removing ", nrow(df.rm), " builds of ", nrow(df.builds), "...")
delete_builds(df.rm$`Build ID`)
