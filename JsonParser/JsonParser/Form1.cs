using System;
using Newtonsoft.Json;
using System.Windows.Forms;

namespace JsonParser
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        #region UI events
        private void cmdDeserialise_Click(object sender, EventArgs e)
        {
            // debugOutput(txtInput.Text);
            deserialiseJSON(txtInput.Text);
        }
        private void cmdClear_Click(object sender, EventArgs e)
        {
            txtDebugOutput.Text = string.Empty;
        }
        #endregion

        #region json functions
        private void deserialiseJSON(string strJSON)
        {
            try
            {
                var jPerson = JsonConvert.DeserializeObject<dynamic>(strJSON);

                debugOutput("Here's our JSON objecdt: " + jPerson.ToString());
            }
            catch(Exception ex)
            {
                debugOutput("We had a problem: " + ex.Message.ToString());
            }
        }
        #endregion

        #region Debug output
        private void debugOutput(string strDebugText)
        {
            try
            {
                System.Diagnostics.Debug.Write(strDebugText + Environment.NewLine);
                txtDebugOutput.Text = txtDebugOutput.Text + strDebugText + Environment.NewLine;
                txtDebugOutput.SelectionStart = txtDebugOutput.TextLength;
                txtDebugOutput.ScrollToCaret();
            }
            catch(Exception ex)
            {
                System.Diagnostics.Debug.Write(ex.Message.ToString() + Environment.NewLine);
            }
        }
        #endregion
    }
}
