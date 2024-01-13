from time import sleep

from selene import browser, have, command
import os

from data.user_data import User


class RegistrationPage:

    def open(self):
        browser.open('automation-practice-form')
        sleep(10)
        browser.all('[id^=google_ads]').with_(timeout=10).wait_until(
            have.size_less_than_or_equal(3)
        )
        browser.all('[id^=google_ads]').perform(command.js.remove)

    def fill_form(self, user: User):
        browser.element('#firstName').type(user.name)
        browser.element('#lastName').type(user.lastname)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.phone)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-dropdown-container').click()
        browser.all('.react-datepicker__month-dropdown-container select option').element_by(
            have.exact_text(user.birthday[1])).click()
        browser.element('.react-datepicker__year-dropdown-container').click()
        browser.all('.react-datepicker__year-select option').element_by(
            have.exact_text(user.birthday[2])).click()
        browser.all(f'.react-datepicker__day--0{user.birthday[0]}').first.click()

        browser.element('#subjectsInput').type('En')

        browser.element('#react-select-2-option-0').should(have.exact_text(user.subjects)).click()

        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobby)).perform(
            command.js.scroll_into_view).click()

        browser.element('#currentAddress').perform(
            command.js.scroll_into_view)
        browser.element('#currentAddress').type(user.address)

        picture_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'resources', user.picture)
        browser.element('#uploadPicture').send_keys(os.path.abspath(picture_path))

        # browser.element('#state').perform(
        #     command.js.scroll_into_view).click()

        browser.element('#state').click().element('#react-select-3-option-2').should(
            have.exact_text(user.state)).click()

        browser.element('#city').click().element('#react-select-4-option-0').should(have.exact_text(user.city)).click()
        browser.element('#submit').press_enter()

    def assert_form(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            ' '.join([user.name, user.lastname]),
            user.email,
            user.gender,
            user.phone,
            f"{user.birthday[0]} {user.birthday[1]},{user.birthday[2]}",
            user.subjects,
            user.hobby,
            user.picture,
            user.address,
            ' '.join([user.state, user.city])))
