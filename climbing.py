#!/usr/bin/python
# filename: climbing.py
# description: A database containing climbing routes around the globe, it gives the ability for users to submit their reviews


import MySQLdb as db
import time
import cgi
import cgitb; cgitb.enable()
import random

print "Content-Type: text/html"
print "" # blank line

################################################################################
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """ 
    # connect to the MYSQL database
    conn = db.connect(host="localhost",
                      user="xiang",
                      passwd="8900",
                      db="xiang")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print """
    <html>
    <head>
    <style>
    body{background-image:url('climbing1.jpg');}
    </style>
    <center><title>%s</title>
    </head>
    <body>
    <h1>%s</h1>
    <img src= %s width=800 height=550</center>
    """ % (title, title,pic)


################################################################################
def doHTMLTail():

    # always show this link to go back to the main page
    print """
    <p>
    <hr>
    <a href="./climbing.py">Return to main page.</a><br>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime()

################################################################################
def debugFormData(form):
    """
    A helper function which will show us all of the form data that was
    sent to the server in the HTTP form.
    """
    
    print """
    <h2>DEBUGGING INFORMATION</h2>
    <p>
    Here are the HTTP form data:
    """
    print """
    <table border=1>
        <tr>
            <th>key name</th>
            <th>value</th>
        </tr>
    """
    
    # form behaves like a python dict
    keyNames = form.keys()
    # note that there is no .values() method -- this is not an actual dict

    ## use a for loop to iterate all keys/values
    for key in keyNames:

        ## discover: do we have a list or a single MiniFieldStorage element?
        if type(form[key]) == list:

            # print out a list of values
            values = form.getlist(key)
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, str(values))

        else:
            # print the MiniFieldStorage object's value
            value = form[key].value
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, value)
        
    print """
    </table>
    <h3>End of HTTP form data</h3>
    <hr>
    """

## end: def debugFormData(form)
################################################################################
def getAllRoutes():
    """
    Middleware function to get all users from the profiles table.
    Returns a list of tuples of (idnum, lastname, firstname).
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT idNum, name, country,rating
    FROM climbingroutes
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getAllUsers():

################################################################################
def getAllUsers():
    """
    Middleware function to get all users from the profiles table.
    Returns a list of tuples of (idnum, lastname, firstname).
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT userid, username, email
    FROM user
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getAllUsers():
################################################################################
def getOneRoute(idNum):
    """
    Middleware function to retrieve one profile record from the database.
    Returns a list containing one tuple.
    """
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM climbingroutes
    WHERE idNum=%s
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

################################################################################
def getOneUser(userid):
    """
    Middleware function to retrieve one profile record from the database.
    Returns a list containing one tuple.
    """
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM user
    WHERE userid=%s
    """

    # execute the query
    parameters = (int(userid), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data
################################################################################
def showRoutePage(data):
    """
    Presentation layer function to display the profile page for one user.
    """

    ## show profile information
    (idNum, name, country, location,climbingarea,rating,routetype,websitelink,pitches) = data[0]

    print """
    <center><h2>%s's Info Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>Country</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Location</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Climbing Area</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Rating</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Route Type</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Number of Pitches</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Mountain Project WebLink</td>
            <td><a href="%s">%s</a></td>

        </tr>
        <tr>
            <td>
            <form>
            <input type="submit" name="beginUpdate" value="update">
            <input type="hidden" name="idNum" value="%s">
            </form>
        </tr>
    </table></center>
    """ %(name,country,location,climbingarea,rating,routetype,pitches,websitelink,websitelink,idNum)

    print"""
    
    <center><h2> Post a new review</h2>
    <p>
    <form method="post" action=climbing.py>
    <input type="hidden" name="idNum" value="%s">
    <label>Compose your review</label><br>
    <input type="text" name="review"><br>
    <label>Insert your userid, if you don't remember, check your update profile page</label><br>
    <input type="text" name="userid"><br>
    <input type="submit" name="post" value="post it!">
    </form></center>

    """ % (data[0][0])

    data=getReviews(idNum)
    showReviews(data)

################################################################################
def showUserPage(data):
    """
    Presentation layer function to display the profile page for one user.
    """

    ## show profile information
    (userid,username,email) = data[0]

    print """
    <center><h2>%s's Personal and Reviews Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>Email</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>
            <form>
            <input type="submit" name="beginUserUpdate" value="update email">
            <input type="hidden" name="userid" value="%s">
            </form>
        </tr>
    </table></center>
    """ %(username,email,userid)

    review=getReviewForUsers(userid)
    showReviewsForUsers(review)
##############################################################################
def showAllRoutes(data):
    """
    Presentation layer function to display a table containing all users' lastnames
    and first names.
    """

    ## create an HTML table for output:
    print """
    <center>
    <h2>Routes List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>Name</b></font></td>
        <td><font size=+1"><b>Country</b></font></td>
        <td><font size=+1"><b>Rating</b></font></td>
      </tr>
    """
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (idNum, name, country,rating) = row

        print """
      <tr>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
      </tr>
        """ % (idNum, name, idNum, country,idNum,rating)

    print """
    </table>
    </center>
    """
        
    print "<center>Found %d routes.<br></center>" % len(data)

## end: def showAllUsers(data):
    
##########################################################################
def showAllUsers(data):
    """
    Presentation layer function to display a table containing all users' lastnames
    and first names.
    """

    ## create an HTML table for output:
    print """
    <center>
    <h2>Routes List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>username</b></font></td>
        <td><font size=+1"><b>email</b></font></td>
      </tr>
    </center>  
    """
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (userid,username,email) = row

        print """
        <center>
      <tr>
        <td><a href="?userid=%s">%s</a></td>
        <td><a href="?userid=%s">%s</a></td>
      </tr>
        </center>  
        """ % (userid, username, userid, email)

    print """
    </table>
    """
        
    print "<center>Found %d routes.<br></center>" % len(data)

## end: def showAllUsers(data):
        
################################################################################
def userbutton():

    print """
<center>
    <form>
        <input type="submit" name="showAllUsers" value="Show all registerd Users">
    </form>
    </center>
    """

################################################################################
def showAddRouteForm():
    print """
<center>
    <h2> Add a new route </h2>
    <form>
    <table border=1>
        <tr>
            <td>Name</td>
            <td><input type="text" name="name"></td>
        </tr>
        <tr>
            <td>Country</td>
            <td><input type="text" name="country"></td>
        </tr>
        <tr>
            <td>Location</td>
            <td><input type="text" name="location"></td>
        </tr>
        <tr>
            <td>Climbing area</td>
            <td><input type="text" name="climbingarea"></td>
        </tr>
        <tr>
            <td>rating</td>
            <td><select name="rating" size="1">
            <option value="3-4">3-4</option>
            <option value="5.0">5.0</option>
            <option value="5.1">5.1</option>
            <option value="5.2">5.2</option>
            <option value="5.3">5.3</option>
            <option value="5.4">5.4</option>
            <option value="5.5">5.5</option>
            <option value="5.6">5.6</option>
            <option value="5.7">5.7</option>
            <option value="5.8">5.8</option>
            <option value="5.9">5.9</option>
            <option value="5.9a">5.9a</option>
            <option value="5.9b">5.9b</option>
            <option value="5.9c">5.9c</option>
            <option value="5.9d">5.9d</option>
            <option value="5.10">5.10</option>
            <option value="5.10a">5.10a</option>
            <option value="5.10b">5.10b</option>
            <option value="5.10c">5.10c</option>
            <option value="5.10d">5.10d</option>
            <option value="5.11">5.11</option>
            <option value="5.11a">5.11a</option>
            <option value="5.11b">5.11b</option>
            <option value="5.11c">5.11c</option>
            <option value="5.11d">5.11d</option>
            <option value="5.12">5.12</option>
            <option value="5.12a">5.12a</option>
            <option value="5.13b">5.13b</option>
            <option value="5.13c">5.13c</option>
            <option value="5.13d">5.13d</option>
            <option value="5.14">5.14</option>
            <option value="5.14a">5.14a</option>
            <option value="5.14b">5.14b</option>
            <option value="5.14c">5.14c</option>
            <option value="5.14d">5.14d</option>
            <option value="5.15">5.15</option>
            <option value="5.15a">5.15a</option>
            <option value="5.15b">5.15b</option>
            <option value="5.15c">5.15c</option>
        </select><br></td>
        </tr>
        <tr>
            <td>routetype</td>
        <td>
            <input type="radio" name="routetype" value="trad"><label>trad</label><br>
            <input type="radio" name="routetype" value="sport"><label>sport</label><br>
            <input type="radio" name="routetype" value="alpine"><label>alpine</label><br>       
            <input type="radio" name="routetype" value="free climbing"><label>free climbing</label><br>
            <input type="radio" name="routetype" value="boulder"><label>boulder</label><br>
        </td>
        </tr>
        <tr>
            <td>pitches</td>
            <td><input type="text" name="pitches"></td>
        </tr>
        <tr>
            <td>Mountain Project Weblink</td>
            <td><input type="checkbox" name="optional" value="Optional weblink"><label>Optional Mountain Project link</label><br>
            <input type="text" name="websitelink" value="-" ><br></td>
        </tr>
        <tr>
            <td><input type="submit" name="insertroute" value="add">
        </td>
            </td>
        </tr>
    </table>
    </form>
    <br>
    </center>
    """
################################################################################
def showAddUserForm():
    print """
    <h2> Add a user </h2>
    <form>
    <table border=1>
        <tr>
            <td>User Name</td>
            <td><input type="text" name="username"></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <td><input type="submit" name="adduser" value="Add User">
        </td>
            </td>
        </tr>
    </table>
    </form>
    <br>
    """
################################################################################
def showUpdateRouteForm(data):

    record= data[0]


    print """
<center>
    <h2> Add a new route </h2>
    <form>
    <table border=1>
        <tr>
            <td>idNum -Do not Change-</td>
            <td><input type="text" name="idNum" value=%s></td>
        </tr>
        <tr>
            <td>Name</td>
            <td><input type="text" name="name" value=%s></td>
        </tr>
        <tr>
            <td>Country</td>
            <td><input type="text" name="country" value=%s></td>
        </tr>
        <tr>
            <td>Location</td>
            <td><input type="text" name="location" value=%s></td>
        </tr>
        <tr>
            <td>Climbing area</td>
            <td><input type="text" name="climbingarea" value=%s></td>
        </tr>
        <tr>
            <td>rating</td>
            <td><select name="rating" size="1">
            <option value=%s>same</option>
            <option value="3-4">3-4</option>
            <option value="5.0">5.0</option>
            <option value="5.1">5.1</option>
            <option value="5.2">5.2</option>
            <option value="5.3">5.3</option>
            <option value="5.4">5.4</option>
            <option value="5.5">5.5</option>
            <option value="5.6">5.6</option>
            <option value="5.7">5.7</option>
            <option value="5.8">5.8</option>
            <option value="5.9">5.9</option>
            <option value="5.9a">5.9a</option>
            <option value="5.9b">5.9b</option>
            <option value="5.9c">5.9c</option>
            <option value="5.9d">5.9d</option>
            <option value="5.10">5.10</option>
            <option value="5.10a">5.10a</option>
            <option value="5.10b">5.10b</option>
            <option value="5.10c">5.10c</option>
            <option value="5.10d">5.10d</option>
            <option value="5.11">5.11</option>
            <option value="5.11a">5.11a</option>
            <option value="5.11b">5.11b</option>
            <option value="5.11c">5.11c</option>
            <option value="5.11d">5.11d</option>
            <option value="5.12">5.12</option>
            <option value="5.12a">5.12a</option>
            <option value="5.13b">5.13b</option>
            <option value="5.13c">5.13c</option>
            <option value="5.13d">5.13d</option>
            <option value="5.14">5.14</option>
            <option value="5.14a">5.14a</option>
            <option value="5.14b">5.14b</option>
            <option value="5.14c">5.14c</option>
            <option value="5.14d">5.14d</option>
            <option value="5.15">5.15</option>
            <option value="5.15a">5.15a</option>
            <option value="5.15b">5.15b</option>
            <option value="5.15c">5.15c</option>
        </select><br></td>
        </tr>
        <tr>
            <td>routetype</td>
        <td>
            <input type="radio" name="routetype" value="%s"><label>same</label><br>
            <input type="radio" name="routetype" value="trad"><label>trad</label><br>
            <input type="radio" name="routetype" value="sport"><label>sport</label><br>
            <input type="radio" name="routetype" value="alpine"><label>alpine</label><br>       
            <input type="radio" name="routetype" value="free climbing"><label>free climbing</label><br>
            <input type="radio" name="routetype" value="boulder"><label>boulder</label><br>
        </td>
        </tr>

        <tr>
            <td>Mountain Project Weblink</td>
            <td><input type="checkbox" name="optional" value="Optional weblink"><label>Optional Mountain Project link</label><br>
            <input type="text" name="websitelink" value="%s" ><br></td>
        </tr>
        <tr>
            <td>pitches</td>
            <td><input type="text" name="pitches" value=%s></td>
        </tr>
        <tr>
            <td><input type="submit" name="updateroute" value="Update">
            <td><input type="submit" name="cancel" value="Cancel Update"></td>
            
        </td>
            </td>
        </tr>
    </table>
    </form>
    <br>
    </center>
    """ %record

################################################################################
def showUpdateUserForm(data):

    record= data[0]


    print """
<center>
    <h2> Add a new route </h2>
    <form>
    <table border=1>
        <tr>
            <td>UserId -Do not Change-</td>
            <td><input type="text" name="userid" value=%s></td>
        </tr>
        <tr>
            <td>Name</td>
            <td><input type="text" name="username" value=%s></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><input type="text" name="email" value=%s></td>
        </tr>
        <tr>
            <td><input type="submit" name="updateuser" value="Update">
            <td><input type="submit" name="cancel" value="Cancel Update"></td>
            
        </td>
    </table>
    </form>
    <br>
    </center>
    """ %record
        
################################################################################


def updateRoute(idNum,name,country,location,climbingarea,rating,routetype,pitches,websitelink):

    # connect to db
    conn, cursor = getConnectionAndCursor()

    
    # prep some SQL
    sql = """
    UPDATE climbingroutes
    SET idNum=%s,
    name=%s,
    country=%s,
    location=%s,
    climbingarea=%s,
    rating=%s,
    routetype=%s,
    websitelink=%s,
    pitches=%s
    WHERE idNum=%s
    """

    parameters=(idNum,name,country,location,climbingarea,rating,routetype,websitelink,pitches,idNum)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount

################################################################################


def updateUser(userid,username,email):

    # connect to db
    conn, cursor = getConnectionAndCursor()

    
    # prep some SQL
    sql = """
    UPDATE user
    SET userid=%s,
    username=%s,
    email=%s
    WHERE userid=%s
    """

    parameters=(userid,username,email,userid)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount
    
################################################################################    
def addRoute(name,country,location,climbingarea,rating,routetype,pitches,websitelink):

    conn, cursor = getConnectionAndCursor()

    sequel1= """
    SELECT max(idNum)
    FROM climbingroutes
    """
    cursor.execute(sequel1)
    maxid=cursor.fetchone()
    maxid=maxid[0]+1
    
    # prep some SQL
    sql = """
    INSERT INTO climbingroutes VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)

    """

    parameters=(maxid,name,country,location,climbingarea,rating,routetype,websitelink,pitches)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount
################################################################################    
def addUser(username,email):

    conn, cursor = getConnectionAndCursor()

    sequel1= """
    SELECT max(idNum)
    FROM climbingroutes
    """
    cursor.execute(sequel1)
    maxid=cursor.fetchone()
    maxid=maxid[0]+1
    
    # prep some SQL
    sql = """
    INSERT INTO user VALUES
    (%s,%s,%s)

    """

    parameters=(maxid,username,email)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount 

################################################################################
def getReviewForUsers(userid):
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM reviews
    WHERE userid=%s
    """

    # execute the query
    parameters = (int(userid), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data
################################################################################
def showReviewsForUsers(review):
    ## show profile information
    print"""
<center>
    <h2>Personal reviews</h2>
    <p>
    </center>
    """
    for row in review:
        
        (DateTime,idNum,review,userid) = row

        print """
<center>
        <table border=1>
            <tr>
                <td>Date</td>
                <td>%s</td>
            </tr>
            <tr>
                <td>Review</td>
                <td>%s</td>
            </tr>
        </table>
        </center>
        """ % (DateTime,review)
################################################################################   
def getReviews(idNum):


    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT r.review, r.DateTime, u.username,u.userid
    FROM reviews r, user u, climbingroutes c
    WHERE c.idNum=%s AND r.idNum=c.idNum AND r.userid=u.userid
    ORDER BY DateTime DESC
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data
################################################################################
def showReviews(data):

    print """
<center>
    <h2>Reviews for this route</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>Review</b></font></td>
        <td><font size=+1"><b>Date</b></font></td>  
        <td><font size=+1"><b>Username</b></font></td>
      </tr></center>
    """
    for row in data:
        
        (review, DateTime,username,userid) = row


        print """<center>
      <tr>
        <td><a href="?userid=%s">%s</a></td>
        <td><a href="?userid=%s">%s</a></td>
        <td><a href="?userid=%s">%s</a></td>
      </tr>
      </center>
        """ % (userid,review,userid,DateTime,userid,username)


    
    print """
    </table>
    """

################################################################################    
def postReview(idNum, review,userid):

    conn, cursor = getConnectionAndCursor()

    tm=time.localtime()
    timestamp= '%04d-%02d-%02d %02d:%02d:%02d' % tm[0:6]
    # prep some SQL
    sql = """
    INSERT INTO reviews VALUES
    (%s,%s,%s,%s)

    """

    parameters=(timestamp,idNum,review,userid)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount        
################################################################################
if __name__ == "__main__":

    # get form field data
    form = cgi.FieldStorage()
    

    number=random.randint(0,9)
    pictures=["climbing2.jpg","climbing3.jpg","climbing4.jpg","climbing5.jpg","climbing6.jpg","climbing7.jpg","climbing8.jpg","climbing9.jpg","climbing10.jpg","climbing11.jpg"]
    pic=pictures[number]
    doHTMLHead("Climbing around the globe")
    if "beginUpdate" in form:
        idNum=form["idNum"].value
        data= getOneRoute(idNum)
        showUpdateRouteForm(data)

    elif "updateroute" in form:
        idNum=form["idNum"].value
        name=form["name"].value
        country=form["country"].value
        location=form["location"].value
        climbingarea=form["climbingarea"].value
        rating=form["rating"].value
        routetype=form["routetype"].value
        websitelink=form["websitelink"].value
        pitches=form["pitches"].value

        rowcount=updateRoute(idNum,name,country,location,climbingarea,rating,routetype,pitches,websitelink)

        print "%d rows were updated.<p>" % rowcount

    elif "beginUserUpdate" in form:
        userid=form["userid"].value
        data= getOneUser(userid)
        showUpdateUserForm(data)

    elif "updateuser" in form:
        userid=form["userid"].value
        username=form["username"].value
        email=form["email"].value
        rowcount= updateUser(userid,username,email)
        print "%d rows were updated.<p>" % rowcount        
                
    elif "idNum" in form:
        idNum=form["idNum"].value
        data=getOneRoute(idNum)
        showRoutePage(data)

        if "post" in form:
            review=form["review"].value
            userid=form["userid"].value
            rowcount=postReview(idNum, review,userid)
            print "%d review published, come back later to see your review!.<p>" % rowcount

    elif "insertroute" in form:
        name=form["name"].value
        country=form["country"].value
        location=form["location"].value
        climbingarea=form["climbingarea"].value
        rating=form["rating"].value
        routetype=form["routetype"].value
        pitches=form["pitches"].value
        websitelink=form["websitelink"].value

        rowcount=addRoute(name,country,location,climbingarea,rating,routetype,pitches,websitelink)
        print "<B> Route added, thank you for your contribution</B>"

    elif "showAllUsers" in form:
        data= getAllUsers()
        showAllUsers(data)
        showAddUserForm()

    elif "userid" in form:
        userid=form["userid"].value
        data= getOneUser(userid)
        showUserPage(data)

    elif "adduser" in form:
        username=form["username"].value
        email=form["email"].value

        rowcount=addUser(username,email)
        print "<B> User added, thank you for joining us</B>"


    else:
        
        data = getAllRoutes()
        showAllRoutes(data)
        showAddRouteForm()
        userbutton()

        

    doHTMLTail() 
