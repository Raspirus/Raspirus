use crate::{
    backend::yara_scanner::{Skipped, TaggedFile},
    frontend::iced::{wrap, Card, Message, Raspirus},
};

impl Raspirus {
    pub fn results(
        &self,
        tagged: Vec<(TaggedFile, bool)>,
        skipped: Vec<(Skipped, bool)>,
    ) -> iced::Element<Message> {
        let top_row = iced::widget::Row::new()
            .push(iced::widget::horizontal_space())
            .push(
                iced::widget::Button::new(
                    iced::widget::Text::new(iced_aw::Bootstrap::House.to_string())
                        .font(iced_aw::BOOTSTRAP_FONT),
                )
                .on_press(Message::OpenMain),
            );
        let mut tagged_list = iced::widget::Column::new()
            .push(iced::widget::Text::new(format!(
                "Found files ({})",
                tagged.len()
            )))
            .spacing(5);

        for (tag, expanded) in tagged {
            //let expanded = *expanded;
            let mut descriptions = iced::widget::Column::new().height(iced::Length::Shrink);

            if expanded {
                // build rules list for each match
                for rule in tag.descriptions.clone() {
                    descriptions = descriptions.push(
                        iced::widget::Row::new()
                            .push(iced::widget::Text::new(rule.rule_name))
                            .push(iced::widget::horizontal_space())
                            .push(iced::widget::Text::new(rule.rule_description)),
                    )
                }
            }

            // build the dropdown
            tagged_list = tagged_list.push({
                let mut card = iced_aw::widgets::Card::new(
                    iced::widget::Row::new()
                        .push(iced::widget::Text::new(format!(
                            "{}",
                            tag.path.to_string_lossy()
                        )))
                        .push(iced::widget::horizontal_space())
                        .push(iced_aw::widgets::Badge::new(iced::widget::Text::new(
                            format!("{}", tag.rule_count),
                        )))
                        .push(
                            iced::widget::Button::new(
                                iced::widget::Text::new(
                                    if expanded {
                                        iced_aw::Bootstrap::CaretDownFill
                                    } else {
                                        iced_aw::Bootstrap::CaretLeftFill
                                    }
                                    .to_string(),
                                )
                                .font(iced_aw::BOOTSTRAP_FONT),
                            )
                            .on_press(Message::ToggleCard {
                                card: Card::Tagged { card: tag.clone() },
                            }),
                        )
                        .push(
                            iced::widget::Button::new(
                                iced::widget::Text::new(
                                    iced_aw::Bootstrap::BoxArrowUpLeft.to_string(),
                                )
                                .font(iced_aw::BOOTSTRAP_FONT),
                            )
                            .on_press(Message::GenerateVirustotal { path: tag.path }),
                        )
                        .spacing(5)
                        .height(iced::Length::Shrink),
                    descriptions,
                );
                if !expanded {
                    card = card
                        .foot(iced::widget::horizontal_space().height(0))
                        .padding_foot(0.into())
                        .padding_body(0.into());
                }
                card
            });
        }

        let mut skipped_list = iced::widget::Column::new()
            .push(iced::widget::Text::new(format!(
                "Skipped files ({})",
                skipped.len()
            )))
            .spacing(5);

        for (skip, expanded) in skipped {
            //let expanded = *expanded;
            let mut description = iced::widget::Column::new().height(iced::Length::Shrink);

            if expanded {
                description = description.push(iced::widget::Text::new(skip.reason.clone()));
            }

            // build the dropdown
            skipped_list = skipped_list.push({
                let mut card = iced_aw::widgets::Card::new(
                    iced::widget::Row::new()
                        .push(iced::widget::Text::new(format!(
                            "{}",
                            skip.path.to_string_lossy()
                        )))
                        .push(iced::widget::horizontal_space())
                        .push(
                            iced::widget::Button::new(
                                iced::widget::Text::new(
                                    if expanded {
                                        iced_aw::Bootstrap::CaretDownFill
                                    } else {
                                        iced_aw::Bootstrap::CaretLeftFill
                                    }
                                    .to_string(),
                                )
                                .font(iced_aw::BOOTSTRAP_FONT),
                            )
                            .on_press(Message::ToggleCard {
                                card: Card::Skipped { card: skip.clone() },
                            }),
                        )
                        .spacing(5)
                        .height(iced::Length::Shrink),
                    description,
                );
                if !expanded {
                    card = card
                        .foot(iced::widget::horizontal_space().height(0))
                        .padding_foot(0.into())
                        .padding_body(0.into());
                }
                card
            });
        }
        iced::widget::Scrollable::new(wrap(
            15,
            iced::widget::Column::new()
                .push(top_row)
                .push(iced::widget::horizontal_rule(5))
                .push(tagged_list)
                .push(iced::widget::horizontal_rule(5))
                .push(skipped_list)
                .spacing(5)
                .into(),
        ))
        .into()
    }
}