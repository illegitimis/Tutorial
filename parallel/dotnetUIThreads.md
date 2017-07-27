# UI Threads

### WinForms

    void GetNewTweet() {
        var tweet = _twitter.GetTweet(); 
        if (InvokeRequired)    
            this.Invoke(new Action(() => listTweets.Items.Add(tweet)));
        else
            listTweets.Items.Add(tweet);
    }


### WPF
This pattern isn’t limited to Windows Forms. The specific way to check the current thread and use the UI thread may vary depending on the type of application you’re using. (WPF) uses `Dispatcher.CheckAccess` and `Dispatcher.Invoke`.

### todo

PostSharp has `UIThread, WorkerThread  : MethodInterceptionAspect`

    public delegate void UIWorkDelegate();

    public static void ExecuteUIWorkAsyncWithDispatchTimer(UIWorkDelegate action) {
	DispatcherTimer timer = new DispatcherTimer { Interval = new TimeSpan(100) };
	timer.Tick += new EventHandler(delegate(object sender, EventArgs e) {
		timer.Stop();
		timer = null;
		action.DynamicInvoke(null);
	});
	timer.Start(); }