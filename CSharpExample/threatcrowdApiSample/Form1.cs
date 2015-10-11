using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.Serialization;
using System.Net;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;



namespace threatcrowdApiSample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            WebClient c = new WebClient();
            var data = c.DownloadString("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=aoldaily.com");
            //Console.WriteLine(data);
            JObject o = JObject.Parse(data);
            Console.WriteLine("Permalink: " + o["permalink"]);
            foreach (string reference in o["references"])
            {
                Console.WriteLine("Reference:" + reference);
            }

        }
    }
}
