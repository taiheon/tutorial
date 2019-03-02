using System;

using Uwp2.ViewModels;

using Windows.UI.Xaml.Controls;

namespace Uwp2.Views
{
    public sealed partial class MainPage : Page
    {
        private MainViewModel ViewModel
        {
            get { return ViewModelLocator.Current.MainViewModel; }
        }

        public MainPage()
        {
            InitializeComponent();
        }
    }
}
