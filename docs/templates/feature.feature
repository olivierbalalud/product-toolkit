# Copied to …/stories/US-012.1-<slug>/features/<name>.feature
# English only, whatever the PRD's source locale [R3-Q1a amendment].
# Domain words use the glossary's English term [R3-C3].
# UI text is referenced by copy-deck key, only where the exact wording matters [R3-C2].
# Tag every scenario with the story and the use-case step or extension it covers [R3-Q1a].
# Frozen at Design-complete: changed later only by a DCR or an amendment [R3-Q1a, R4-Q8e′].

@US-012.1
Feature: Book a meeting room
  As an employee
  I want to book a free meeting room
  So that my team has a place to meet without double bookings

  Background:
    Given I am signed in as an employee

  @UC-012.1
  Scenario: Book a free room
    When I book a free room for one hour
    Then the booking is listed as "confirmed"
    And the "bookings.new.success" message is shown

  @UC-012.2a
  Scenario: Reject a booking that is too long
    When I book a free room for longer than the maximum duration
    Then no booking is created
    And the "bookings.new.error.tooLong" message is shown

  @UC-012.3a
  Scenario: Reject a room that was booked meanwhile
    Given another employee books the same room for the same hour first
    When I confirm my booking
    Then no booking is created for me
    And the "bookings.new.error.taken" message is shown

  @UC-012.2b
  Scenario: Refuse a booking without permission
    Given I am signed in as a visitor
    When I try to book a free room
    Then the booking is refused
