querystring = require('querystring');
http = require('http');
fs = require 'fs'
{exec} = require 'child_process'
filewalk = require 'file'
connect = require 'connect'

writeBucket = "user7"
url = "codeskulptor-"+writeBucket+".commondatastorage.googleapis.com"
googleid = "GOOGOC4O3IBWEZMQYHRU"
policy = "eyJleHBpcmF0aW9uIjogIjIwMTMtMDEtMDFUMTI6MDA6MDAuMDAwWiIsCgogICJjb25kaXRpb25zIjogWwogICAgeyJidWNrZXQiOiAiY29kZXNrdWxwdG9yLXVzZXI3In0sCiAgICBbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAidXNlcjciXSwKICAgIFsiZXEiLCAiJENvbnRlbnQtVHlwZSIsICJ0ZXh0L3gtcHl0aG9uIl0sCiAgICBbImNvbnRlbnQtbGVuZ3RoLXJhbmdlIiwgMCwgNjU1MzZdCiAgXQp9Cg=="
signature = "9X11uqAtlx4X050KJrANEeeFGg4="

option '-s', '--source [DIR]', 'python source code directory'

PostCode = (filename,codestring) ->
  key = filename

  post_data = """
  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="key"


  """+key+"""

  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="Content-Type"

  text/x-python
  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="GoogleAccessId"


  """+googleid+"""

  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="Policy"


  """+policy+"""

  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="Signature"


  """+signature+"""

  ------WebKitFormBoundaryg5KeYDupWKAqnxs4
  Content-Disposition: form-data; name="file"


  """+codestring+"""

  ------WebKitFormBoundaryg5KeYDupWKAqnxs4--
  """

  post_options =
    host: url
    port: "80"
    path: "/"
    method: "POST"
    headers:
      "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryg5KeYDupWKAqnxs4"
      "Content-Length": post_data.length

  post_req = http.request post_options, (res) ->
    res.setEncoding 'utf8'
    res.on 'data', (chunk) ->
      console.log 'Response: ' + chunk

  post_req.write(post_data)
  post_req.end()

#traslated from codeskulptor.js
createHash = (a) ->
  c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  d = ""
  for b in [0...10]
    d += c.charAt(Math.random() * c.length | 0)
  return d

task 'concatupload', "concat files and upload them to codeskulptor, then opens chrome window", (options) ->

  console.log "Concatenating files"

  appFiles = []

  filewalk.walkSync options.source, (dirPath, dirs, files) ->
    for f in files
      appFiles.push("#{dirPath}/#{f}")

  appContents = new Array
  remaining = appFiles.length

  for file, index in appFiles then do (file, index) ->
    fs.readFile "#{file}", 'utf8', (err, fileContents) ->
      throw err if err

      #if file name isn't __init__.py remove all import lines
      console.log file
      if file.indexOf("__init__") == -1
        filteredContents = fileContents.replace(/import (.*)/g,"")
      else
        filteredContents = fileContents

      appContents[index] = filteredContents
      process() if --remaining is 0

  process = ->
    testCode = appContents.join('\n\n')

    hash = createHash 10
    key = "user7-"+hash+"-0.py"

    console.log "Uploading file"
    PostCode(key,testCode)

    console.log("Filename:"+key)

    console.log("Opening browser")
    exec "open http://www.codeskulptor.org/#"+key