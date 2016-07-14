import os
import inspect
from unittest import TestCase
import operator
from pyradioconfig import pycalcmodel

class TestUtils(TestCase):

    # Hack override used to allow the test to run from python console
    def runTest( self ):
        self.failUnless( True is True )

    # Test loading a module with path
    def test_export_html(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(current_path, "calculated_output\\dumbo_A0_type.xml")
        output_path = os.path.join(current_path, "calculated_output\\dumbo_A0_type.html")

        model = pycalcmodel.ModelRootTypeXml(input_path)

        html = '<html><body>\n'
        html += '<h1>Radio Configurator Types</h1>\n'
        html += '<hr>\n'
        html += '<h2>Table of Contents:</h2>\n'
        html += """
            <ul>
              <li><a href="#profiles">Profiles:</a></li>
              <ul>
              """
        for profile in sorted(model.profiles, key=lambda profile: profile.name):
            html += '<li><a href="#' +  profile.name + '">' + profile.name + '</a></li>\n'

        html += '</ul>\n'

        html += """
              <li><a href="#phys">PHY Names</a></li>
            </ul>
        \n"""
        html += self.generate_stylesheet()
        for profile in sorted(model.profiles, key=lambda profile: profile.name):
            html += '<hr>\n'
            html += '<a name="' + profile.name + '"></a>\n'
            html += '<h2>Profile Name: ' + profile.name + '</h2>\n'
            html += """
            <h3>Inputs:</h3>
            <table>
                 <tr>
                   <th>Category</th>
                   <th>Name</th>
                   <th>Description</th>
                   <th>Type</th>
                 </tr>
                """
            for input in sorted(profile.inputs, key=lambda input: (input.category, input.var_name)):
                html += '<tr>\n'
                html += '<td>{0}</td>\n'.format(input.category)
                html += '<td>{0}</td>\n'.format(input.var_name)
                html += '<td>{0}</td>\n'.format(input.readable_name)
                html += '<td>{0}</td>\n'.format(input.input_type)
                html += '</tr>\n'

            html += """
            </table>
            """

            html += """
            <h3>Outputs:</h3>
            <table>
                 <tr>
                   <th>Category</th>
                   <th>Name</th>
                   <th>Description</th>
                   <th>Type</th>
                 </tr>
                """
            for output in sorted(profile.outputs, key=lambda output: (output.category, output.var_name)):
                html += '<tr>\n'
                html += '<td>{0}</td>\n'.format(output.category)
                html += '<td>{0}</td>\n'.format(output.var_name)
                html += '<td>{0}</td>\n'.format(output.readable_name)
                html += '<td>{0}</td>\n'.format(output.output_type)
                html += '</tr>\n'

            html += """
            </table>
            """

        html += '<hr>\n'
        html += '<a name="phys"></a>\n'
        html += '<h2>PHY Names</h2>\n'
        html += """
        <table>
             <tr>
               <th>Group</th>
               <th>Name</th>
               <th>Description</th>
             </tr>
            """
        for phy in sorted(model.phys, key=lambda phy: (phy.group_name, phy.name)):
            html += '<tr>\n'
            html += '<td>{0}</td>\n'.format(phy.group_name)
            html += '<td>{0}</td>\n'.format(phy.name)
            html += '<td>{0}</td>\n'.format(phy.readable_name)
            html += '</tr>\n'

        html += """
        </table>
        """
        html += '</body></html>\n'

        file = open(output_path, 'w')
        file.write(html)
        file.close()


    def generate_stylesheet(self):
        style_str = """
<style media="screen" type="text/css">
body {
   background-color: #eee;
   font: 82.5%/1.3 Verdana, Arial, Helvetica, sans-serif; }
#wrap {
   font-size: 130%;
   width: 550px;
   padding: 10px 50px;
   margin: 0 auto;
   border: 1px solid #ccc;
   background-color: #fff;}

/* Table Styles */
table {
   width: 80%;
   border: 1px solid #000000;
   margin: 1em 25px;
   text-align: left; }
th {
   font-weight: bold;
   background-color: #acf;
   border-bottom: 1px solid #feef; }
td,th {
   padding: 4px 5px;
   border: 1px solid #000000;
   }
.odd {
   background-color: #eef; }
.odd td {
   border-bottom: 0px solid #000000; }
</style>
    """
        return style_str