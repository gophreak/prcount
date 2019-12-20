# items should be an array of item, which requires the following fields:
  # name - used to display the name as a key for the count
  # count - the number ti display
  # url - the link to the page, if count > 0

def summary(key, items, threshold):
  total = sum(item.count for item in items)
  row = "%s: (%d)" % (key, total)
  if total >= threshold:
    row += " | color=red"

  print(row)

def newOption():
  print('---')

def each(items):
  for item in items:
    row = "%s (%d)" % (item.name, item.count)
    if item.count > 0:
      row += " | href=%s" % (item.url)

    print(row)
