# Task 1: software configuration #
<h3>Subtask 1: Why did I choose to participate in the Dare IT Challenge?</h3> 
<p> Hello my name is Nataliia. 
<img src="https://github.githubassets.com/images/icons/emoji/unicode/1f44b.png" width="20px" alt="wave"/>
I've got a good feedback on the Dare IT Challenge from a friend of mine, so I decided to take part in this program.</p>
<p>I believe that this is a good opportunity to expand my knowledge about testing and start my path as a specialist in this field. I consider the advice of experts to be a significant help in this. Participation in the Dare IT Challenge is also a valuable opportunity to join the community of testers and gain experience as an Automation/Manual tester. During the Challenge, I expect to create a testing project that would contribute to my portfolio.</p>
<h3 style="text-align: right"><i>Nataliia</i></h3>

<hr>

# Task 2: selectors #
<h3>Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.</h3>

<span style="color: slategray"> <i>English version of the web-site: https://scouts-test.futbolkolektyw.pl/en/login?redirected=true</i></span>

<b>scout_panel_heading_xpath</b>
<ol>
<li>//h5</li>
<li>//h5[contains(text(), "Panel")]</li>
<li>//*[contains(@class, "MuiTypography-h5")]</li>
<li>//*[text()="Scouts Panel"]</li>
</ol>

<b>login_xpath></b>
<ol>
<li>//*[@id="login-label"]</li>
<li>//*[text()="Login"]</li>
<li>//*[@for="login"]</li>
</ol>

<b>login_field_xpath</b>
<ol>
<li>//*[@id="login"]</li>
<li>//*[@name="login"]</li>
<li>//*[@type="text"]</li>
</ol>

<b>password_xpath></b>
<ol>
<li>//*[@id="password-label"]</li>
<li>//*[text()="Password"]</li>
<li>//*[@for="password"]</li>
</ol>

<b>password_field_xpath</b>
<ol>
<li>//*[@id="password"]</li>
<li>//*[@name="password"]</li>
<li>//*[@type="password"]</li>
</ol>

<b>remind_password_hyperlink_xpath</b>
<ol>
<li>//a[contains(text(), "Remind")]</li>
<li>//a[@tabindex="-1"]</li>
<li>//*[@id="__next"]//div[1]/a</li>
</ol>

<b>language_dropdown_xpath</b>
<ol>
<li>//div[@tabindex="0"]</li>
<li>//*[@role="button"]</li>
<li>//*[@aria-haspopup="listbox"]</li>
<li>//*[text()="English"]</li>
</ol>

<b>sign_in_button_xpath</b>
<ol>
<li>//*[text()="Sign in"]</li>
<li>//*[@type="submit"]/span[1]</li>
<li>//*[@class="MuiButton-label"]</li>
</ol>


<span style="color: slategray"><i>*dropdown is open:</i></span>

<b>language_dropdown_english_xpath</b>
<ol>
<li>//ul/li[2]</li>
<li>//li[@tabindex="0"]</li>
<li>//*[@data-value="en"]</li>
</ol>

<b>language_dropdown_polish_xpath</b>
<ol>
<li>//ul/li[1]</li>
<li>//li[@tabindex="-1"]</li>
<li>//*[@data-value="pl"]</li>
</ol>

<hr>
<span style="color: slategray"> <i>Polish version of the web-site: https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true</i></span>

<b>language_polish_xpath</b>
<ol>
<li>//div[@tabindex="0"]</li>
<li>//*[@role="button"]</li>
<li>//*[@aria-haspopup="listbox"]</li>
<li>//*[text()="Polski"]</li>
</ol>

<b>password_polish_xpath</b>
<ol>
<li>//*[@id="password-label"]</li>
<li>//*[@for="password"]</li>
<li>//*[text()="Hasło"]</li>
</ol>

<b>remind_password_hyperlink_polish_xpath</b>
<ol>
<li>//*[contains(@class, "jss4")]</li>
<li>//a[contains(text(), "Przypomnij")]</li>
<li>//a[@tabindex="-1"]</li>
<li>//*[@id="__next"]//div[1]/a</li>
</ol>

<b>sign_in_button_polish_xpath</b>
<ol>
<li>//*[text()="Zaloguj"]</li>
<li>//*[@type="submit"]/span[1]</li>
<li>//*[@class="MuiButton-label"]</li>
</ol>

