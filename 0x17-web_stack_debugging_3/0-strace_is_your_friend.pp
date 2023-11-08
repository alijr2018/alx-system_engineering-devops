#find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet 

file { 'fix':
ensure  => file,
content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
}
