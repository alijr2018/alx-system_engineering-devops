#!/usr/bin/env ruby

def match_school(arg)
    # Define the regular expression pattern to match "School"
    regex = /School/
  
    # Use the `=~` operator to check if the argument contains the pattern
    if arg =~ regex
      puts arg.gsub(regex, 'School') # Replace matched "School" with "School"
    else
      puts "$" # If the pattern is not found, print "$"
    end
  end
  
  # Accept one argument from the command line
  if ARGV.empty?
    puts "Usage: #{$PROGRAM_NAME} <string>"
  else
    match_school(ARGV[0])
  end